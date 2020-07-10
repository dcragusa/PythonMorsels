from itertools import zip_longest

class Unpacker(dict):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def __getattr__(self, key):
        if key in self:
            return super().__getitem__(key)

    def __setattr__(self, key, value):
        super().__setitem__(key, value)

    def __iter__(self):
        for value in self.values():
            yield value

    def __getitem__(self, item):
        if isinstance(item, tuple):
            return tuple(self[key] for key in item)
        else:
            return super().__getitem__(item)

    def __setitem__(self, key, value):
        if isinstance(key, tuple):
            sentinel = object()
            for combo in zip_longest(key, value, fillvalue=sentinel):
                # raise an error if we find the sentinel value in the combo:
                # this means we have exhausted either the key or value tuple
                # i.e. they aren't of the same length
                if sentinel in combo:
                    raise ValueError('Keys and values not the same length')
                setattr(self, *combo)
        else:
            return setattr(self, key, value)

    def __repr__(self):
        str_list = [f'{key}={repr(value)}' for key, value in self.items()]
        return f'Unpacker({", ".join(str_list)})'

