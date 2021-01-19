from collections.abc import Sequence


class SliceView(Sequence):
    def __init__(self, sequence, start=None, stop=None, step=None):
        self.sequence = sequence
        self.range = range(*slice(start, stop, step).indices(len(sequence)))

    def __len__(self):
        return len(self.range)

    def __getitem__(self, item):
        if isinstance(item, slice):
            return SliceView(self, item.start, item.stop, item.step)
        return self.sequence[self.range[item]]


class ChainSequence(Sequence):
    def __init__(self, *sequences):
        self.sequences = list(sequences)

    def __repr__(self):
        return f'ChainSequence({", ".join(repr(s) for s in self.sequences)})'

    def __len__(self):
        return sum(len(s) for s in self.sequences)

    def __getitem__(self, item):
        if isinstance(item, slice):
            return SliceView(self, item.start, item.stop, item.step)

        if item < 0:
            item += len(self)
        elif item >= len(self):
            raise IndexError('index out of range')

        for sequence in self.sequences:
            if item < len(sequence):
                return sequence[item]
            item -= len(sequence)

    def __add__(self, other):
        return ChainSequence(*self.sequences, other)

    def __iadd__(self, other):
        self.sequences.append(other)
        return self
