
class cached_property:
    def __init__(self, func):
        self._getter = func
        self._setter = self._deleter = None
        self.name = None

    def setter(self, setter):
        self._setter = setter
        return self

    def deleter(self, deleter):
        self._deleter = deleter
        return self

    def __get__(self, obj, obj_type):
        if obj is None:
            return self
        if self.name in obj.__dict__:
            value = obj.__dict__[self.name]
        else:
            value = self._getter(obj)
        obj.__dict__[self.name] = value
        return value

    def __set__(self, obj, value):
        if self._setter:
            self._setter(obj, value)
            obj.__dict__.pop(self.name, None)
        else:
            obj.__dict__[self.name] = value

    def __delete__(self, obj):
        obj.__dict__.pop(self.name, None)
        if self._deleter:
            self._deleter(obj)

    def __set_name__(self, obj, name):
        self.name = name
