class OrderedSet:
    def __init__(self, iterable):
        # take advantage of the fact that in Py3.6+ dicts are ordered
        self.data = {i: None for i in iterable}

    def __len__(self):
        return len(self.data.keys())

    def __contains__(self, item):
        return item in self.data

    def __getitem__(self, key):
        return list(self.data)[key]

    def __eq__(self, other):
        if isinstance(other, OrderedSet):
            return list(self.data) == list(other.data)
        elif isinstance(other, set):
            return set(self.data) == other
        else:
            return False

    def add(self, item):
        self.data[item] = None

    def discard(self, item):
        if item in self.data:
            del self.data[item]
