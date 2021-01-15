from collections.abc import Sequence
from itertools import zip_longest


class SequenceZip(Sequence):
    def __init__(self, *args):
        self.sequences = args

    def __repr__(self):
        return f'SequenceZip({", ".join(map(repr, self.sequences))})'

    def __len__(self):
        return min(map(len, self.sequences))

    @property
    def len_aware_sequences(self):
        return tuple(seq[:len(self)] for seq in self.sequences)

    def __getitem__(self, idx):
        if isinstance(idx, slice):
            args = [[seq[i] for i in range(*idx.indices(len(self)))] for seq in self.len_aware_sequences]
            return SequenceZip(*args)
        return tuple(s[idx] for s in self.len_aware_sequences)

    def __eq__(self, other):
        if not isinstance(other, SequenceZip):
            return NotImplemented
        sentinel = object()
        for a, b in zip_longest(self.len_aware_sequences, other.len_aware_sequences, fillvalue=sentinel):
            if a is sentinel or b is sentinel or a != b:
                return False
        return True
