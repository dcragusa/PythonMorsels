import math


class FloatRange:
    def __init__(self, n1, n2=None, step=1):
        self.start = 0.0 if n2 is None else n1
        self.end = n1 if n2 is None else n2
        self.step = step

    def __iter__(self):
        n = self.start
        for _ in range(len(self)):
            yield n
            n += self.step

    def __reversed__(self):
        n = self.start + (self.step * (len(self) - 1))
        for _ in range(len(self)):
            yield n
            n -= self.step

    def __len__(self):
        length = (self.end - self.start) / self.step
        return math.ceil(length) if length > 0 else 0

    def __eq__(self, other):
        if not hasattr(other, '__iter__'):
            # oher object is not iterable, cannot compare
            return NotImplemented

        # we just need to compare first, last and step
        # can't use our attributes because we need to compare to ranges
        # this won't work with 1-length lists with different steps
        if len(self) == len(other) <= 1:
            return list(self) == list(other)
        return (
            next(iter(self)) == next(iter(other)) and
            next(reversed(self)) == next(reversed(other)) and
            self.step == other.step
        )


# test while keeping class name camelcase
float_range = FloatRange
