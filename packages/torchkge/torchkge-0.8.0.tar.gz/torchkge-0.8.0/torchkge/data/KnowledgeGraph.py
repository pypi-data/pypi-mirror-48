# -*- coding: utf-8 -*-
"""
Copyright TorchKGE developers
aboschin@enst.fr
"""

from torch import empty, tensor, cat, bernoulli, ones, randint
from torch.utils.data import Dataset

from torchkge.data.utils import get_dictionaries, get_bern_probs

from tqdm import tqdm
from collections import defaultdict


class KnowledgeGraph(Dataset):
    """Knowledge graph representation.

        Parameters
        ----------
        df: pandas Dataframe
            Data frame containing three columns [from, to, rel].
        ent2ix: dict, optional
            Dictionary mapping entity labels to their integer key.
        rel2ix: dict, optional
            Dictionary mapping relation labels to their integer key.

        Attributes
        ----------
        ent2ix: dict
            Dictionary mapping entity labels to their integer key.
        rel2ix: dict
            Dictionary mapping relation labels to their integer key.
        n_ent: int
            Number of distinct entities in the data set.
        n_rel: int
            Number of distinct entities in the data set.
        n_sample: int
            Number of samples in the data set. A sample is a fact: a triplet (h, r, l).
        head_idx: torch.Tensor, dtype = long, shape = (n_sample)
            List of the int key of heads for each sample (fact).
        tail_idx: torch.Tensor, dtype = long, shape = (n_sample)
            List of the int key of tails for each sample (facts).
        relations: torch.Tensor, dtype = long, shape = (n_sample)
            List of the int key of relations for each sample (facts).
        bern_probs: torch.Tensor, dtype = float, shape = (n_sample)
            List of the Bernoulli probabilities for sampling head or tail for each relation\
            (cf. Wang et al. (2014) https://www.aaai.org/ocs/index.php/AAAI/AAAI14/paper/view/8531)

    """

    def __init__(self, df=None, kg=None,
                 ent2ix=None, rel2ix=None, dict_of_heads=None, dict_of_tails=None):

        if ent2ix is None:
            self.ent2ix = get_dictionaries(df, ent=True)
        else:
            self.ent2ix = ent2ix

        if rel2ix is None:
            self.rel2ix = get_dictionaries(df, ent=False)
        else:
            self.rel2ix = rel2ix

        self.n_ent = max(self.ent2ix.values()) + 1
        self.n_rel = max(self.rel2ix.values()) + 1

        if df is not None:
            assert kg is None
            self.n_sample = len(df)
            self.head_idx = tensor(df['from'].map(self.ent2ix).values).long()
            self.tail_idx = tensor(df['to'].map(self.ent2ix).values).long()
            self.relations = tensor(df['rel'].map(self.rel2ix).values).long()
            self.evaluate_bern_probs(df)
        else:
            assert kg is not None
            self.n_sample = kg['heads'].shape[0]
            self.head_idx = kg['heads']
            self.tail_idx = kg['tails']
            self.relations = kg['relations']
            self.bern_probs = kg['bern_probs']

        if dict_of_heads is None or dict_of_tails is None:
            self.dict_of_heads = defaultdict(list)
            self.dict_of_tails = defaultdict(list)
            print('Evaluating dictionaries of possible heads and tails for relations.')
            self.evaluate_dicts()

        else:
            self.dict_of_heads = dict_of_heads
            self.dict_of_tails = dict_of_tails

    def __len__(self):
        return self.n_sample

    def __getitem__(self, item):
        return self.head_idx[item].item(), self.tail_idx[item].item(), self.relations[item].item()

    def split_kg(self, share=0.8, train_size=None):
        """Split the knowledge graph into train and test.

        Parameters
        ----------
        share: float
            Percentage to allocate to train set.
        train_size: integer
            Length of the training set. If this is not None, the first values of the knowledge\
            graph will be used as training set and the rest as test set.

        Returns
        -------
        train_kg: torchkge.data.KnowledgeGraph
        test_kg: torchkge.data.KnowledgeGraph

        """

        if train_size is None:
            mask = (empty(self.head_idx.shape).uniform_() < share)
        else:
            mask = cat([tensor([1 for _ in range(train_size)]),
                        tensor([0 for _ in range(self.head_idx.shape[0] - train_size)])])
            mask = mask.byte()

        train_kg = KnowledgeGraph(
            kg={'heads': self.head_idx[mask],
                'tails': self.tail_idx[mask],
                'relations': self.relations[mask],
                'bern_probs': self.bern_probs},
            ent2ix=self.ent2ix, rel2ix=self.rel2ix,
            dict_of_heads=self.dict_of_heads,
            dict_of_tails=self.dict_of_tails)

        test_kg = KnowledgeGraph(
            kg={'heads': self.head_idx[~mask],
                'tails': self.tail_idx[~mask],
                'relations': self.relations[~mask],
                'bern_probs': self.bern_probs},
            ent2ix=self.ent2ix, rel2ix=self.rel2ix,
            dict_of_heads=self.dict_of_heads,
            dict_of_tails=self.dict_of_tails)

        return train_kg, test_kg

    def evaluate_dicts(self):
        """Evaluate dicts of possible alternatives to an entity in a fact that still gives a true\
        fact in the entire knowledge graph.

        """

        for i in tqdm(range(self.n_sample)):
            self.dict_of_heads[(self.tail_idx[i].item(),
                                self.relations[i].item())].extend([self.head_idx[i].item()])
            self.dict_of_tails[(self.head_idx[i].item(),
                                self.relations[i].item())].extend([self.tail_idx[i].item()])

    def evaluate_bern_probs(self, df):
        """Evaluate the Bernoulli probabilities for negative sampling as in the TransH original\
        paper by Wang et al. (2014) https://www.aaai.org/ocs/index.php/AAAI/AAAI14/paper/view/8531.

        Parameters
        ----------
        df: pandas.DataFrame
            DataFrame from which the torchkge.data.KnowledgeGraph object is built.

        """
        bern_probs = get_bern_probs(df)
        assert len(bern_probs) == len(self.rel2ix)
        bern_probs = {self.rel2ix[rel]: bern_probs[rel] for rel in bern_probs.keys()}
        self.bern_probs = tensor([bern_probs[k] for k in sorted(bern_probs.keys())]).float()

    def corrupt_batch(self, heads, tails, relations, n_ent, sampling='uniform'):
        """For each golden triplet, produce a corrupted one not different from any other golden\
        triplet.

        Parameters
        ----------
        heads: torch.Tensor, dtype = long, shape = (batch_size)
            Tensor containing the integer key of heads of the relations in the current batch.
        tails: torch.Tensor, dtype = long, shape = (batch_size)
            Tensor containing the integer key of tails of the relations in the current batch.
        relations: torch.Tensor, dtype = long, shape = (batch_size)
            Tensor containing the integer key of relations in the current batch.
        n_ent: int
            Number of entities in the entire dataset.
        sampling: str
            Specifies the way of sampling head or tail when choosing the one to corrupt. Either\
            'uniform' or 'bernoulli'.

        Returns
        -------
        neg_heads: torch.Tensor, dtype = long, shape = (batch_size)
            Tensor containing the integer key of negatively sampled heads of the relations\
            in the current batch.
        neg_tails: torch.Tensor, dtype = long, shape = (batch_size)
            Tensor containing the integer key of negatively sampled tails of the relations\
            in the current batch.
        """
        assert sampling in ['uniform', 'bernoulli']
        use_cuda = heads.is_cuda
        assert (use_cuda == tails.is_cuda)
        if use_cuda:
            device = 'cuda'
        else:
            device = 'cpu'

        batch_size = heads.shape[0]
        neg_heads, neg_tails = heads.clone(), tails.clone()

        # Randomly choose which samples will have head/tail corrupted
        if sampling == 'uniform':
            mask = bernoulli(ones(size=(batch_size,), device=device) / 2).double()
        else:
            mask = bernoulli(self.bern_probs[relations]).double()
        n_heads_corrupted = int(mask.sum().item())
        neg_heads[mask == 1] = randint(1, n_ent, (n_heads_corrupted,), device=device)
        neg_tails[mask == 0] = randint(1, n_ent, (batch_size - n_heads_corrupted,), device=device)

        return neg_heads.long(), neg_tails.long()
