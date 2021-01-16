from contextlib import contextmanager

DEFAULTDELTA = 0.0000001


class Comparator:

    defaultdelta = DEFAULTDELTA

    def __init__(self, num, delta=None):
        # we can't put delta=defaultdelta, as default kwargs are bound at definition time
        self.num = num
        self.delta = self.defaultdelta if delta is None else delta

    def __eq__(self, other):
        return abs(self.num - other) <= self.delta

    def __repr__(self):
        return f'Comparator({self.num}, delta={self.delta})'

    def __add__(self, other):
        if isinstance(other, Comparator):
            return Comparator(self.num + other.num, max(self.delta, other.delta))
        else:
            return Comparator(self.num + other, self.delta)

    def __radd__(self, other):
        return Comparator(other + self.num, self.delta)

    def __sub__(self, other):
        if isinstance(other, Comparator):
            return Comparator(self.num - other.num, max(self.delta, other.delta))
        else:
            return Comparator(self.num - other, self.delta)

    def __rsub__(self, other):
        return Comparator(other - self.num, self.delta)

    @classmethod
    @contextmanager
    def default_delta(cls, temp_defaultdelta):
        cls.defaultdelta = temp_defaultdelta
        try:
            yield
        finally:
            cls.defaultdelta = DEFAULTDELTA
