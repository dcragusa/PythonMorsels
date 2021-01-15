from collections.abc import Sequence


class CyclicList(Sequence):

    def __init__(self, iterable):
        self.iterable = list(iterable)

    def __getitem__(self, item):
        if isinstance(item, int):
            return self.iterable[item % len(self.iterable)]
        else:
            start = item.start if item.start is not None else 0
            stop = item.stop if item.stop is not None else (0 if start < 0 else len(self.iterable))
            return [self.iterable[i % len(self.iterable)] for i in range(start, stop)]

    def __setitem__(self, key, value):
        self.iterable[key % len(self.iterable)] = value

    def __len__(self):
        return len(self.iterable)

    def append(self, item):
        self.iterable.append(item)

    def pop(self, index=-1):
        return self.iterable.pop(index)
