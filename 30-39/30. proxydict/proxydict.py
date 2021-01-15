from collections import Mapping, ChainMap


class ProxyDict(Mapping):

    def __init__(self, *maps):
        self.maps = list(maps)
        self.mapping = ChainMap(*self.maps[::-1])

    def __iter__(self):
        for key in self.mapping:
            yield key

    def __len__(self):
        return len(self.mapping)

    def __getitem__(self, key):
        return self.mapping[key]

    def __repr__(self):
        return f'ProxyDict({", ".join(repr(map_) for map_ in self.maps)})'
