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
