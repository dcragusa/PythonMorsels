# I actually already had written something similar to this 2 years ago at
# https://gist.github.com/dcragusa/389c07b5140b0f36e7874d1181f87600

# class EasyDict(dict):
#     # access data by dot notation e.g. {'a': 1} -> d.a = 1
#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         self.__dict__ = self

# we get bonuses 1 and 2 for free!


class EasyDict(dict):
    # access data by dot notation e.g. {'a': 1} -> d.a = 1
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__dict__ = self
        self.normalize = kwargs.get('normalize', False)

    def __getattr__(self, name):
        if self.normalize:
            name = name.replace('_', ' ')
        if name in self:
            return self[name]
        else:
            raise AttributeError

    def __setattr__(self, key, value):
        if key in ['__dict__', 'normalize']:
            super().__setattr__(key, value)
        elif self.normalize:
            self[key.replace('_', ' ')] = value
        else:
            self[key] = value
