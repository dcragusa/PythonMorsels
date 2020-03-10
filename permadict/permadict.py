
class PermaDict(dict):

    def __init__(self, *args, **kwargs):
        self.silent = kwargs.pop('silent', False)
        super().__init__(*args, **kwargs)

    def __setitem__(self, key, value):
        if key in self:
            if not self.silent:
                raise KeyError(f'{repr(key)} already in dictionary')
        else:
            super().__setitem__(key, value)

    def update(self, other=None, **kwargs):
        if kwargs.pop('force', False):
            super().update(**kwargs) if other is None else super().update(other)
        elif other is None:
            for key in kwargs:
                self[key] = kwargs[key]
        elif hasattr(other, 'keys'):
            for key in other.keys():
                self[key] = other[key]
        else:
            for item in other:
                self[item[0]] = item[1]

    def force_set(self, key, value):
        super().__setitem__(key, value)
