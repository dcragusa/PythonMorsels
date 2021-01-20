from collections.abc import MutableSequence


class SequenceZip(MutableSequence):
    def __init__(self, *args):
        self.sequences = args

    def __repr__(self):
        return f'SequenceZip({", ".join(repr(s) for s in self.sequences)})'

    def __len__(self):
        return min(map(len, self.sequences))

    @property
    def len_aware_sequences(self):
        return tuple(s[:len(self)] for s in self.sequences)

    def __getitem__(self, item):
        if isinstance(item, slice):
            return SequenceZip(*(s[item] for s in self.len_aware_sequences))
        if item < 0:
            item += len(self)
        elif item >= len(self):
            raise IndexError
        return tuple(s[item] for s in self.sequences)

    def __eq__(self, other):
        if not isinstance(other, SequenceZip):
            return NotImplemented
        return len(self) == len(other) and all(self[idx] == other[idx] for idx in range(len(self)))

    def __setitem__(self, idx, value):
        if idx < 0:
            idx += len(self)
        elif idx >= len(self):
            raise IndexError
        if len(value) != len(self.sequences):
            raise IndexError
        for val, s in zip(value, self.sequences):
            s[idx] = val

    def __delitem__(self, idx):
        if idx < 0:
            idx += len(self)
        elif idx >= len(self):
            raise IndexError
        for s in self.sequences:
            del s[idx]

    def insert(self, idx, value):
        if idx < 0:
            idx += len(self)
        elif idx >= len(self):
            raise IndexError
        if len(value) != len(self.sequences):
            raise IndexError
        for val, s in zip(value, self.sequences):
            s.insert(idx, val)

    def append(self, value):
        len_self = len(self)  # cache min length as we will change it in the function
        if len(value) != len(self.sequences):
            raise IndexError
        for val, s in zip(value, self.sequences):
            if len(s) == len_self:
                # if this sequence is the minimum length, we append
                s.append(val)
            else:
                # otherwise we change the appropriate item
                s[len_self] = val
