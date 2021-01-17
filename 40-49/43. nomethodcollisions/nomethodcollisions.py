
class NoMethodCollisionsDict(dict):
    def __setitem__(self, key, val):
        # we check if the value is a callable or has a __get__ method (is a descriptor), and is not a property
        if key in self and (callable(val) or hasattr(val, '__get__')) and not isinstance(val, property):
            raise TypeError(f'{key} already defined in class')
        super().__setitem__(key, val)


class NoMethodCollisionsMetaClass(type):
    @classmethod
    def __prepare__(cls, *args):
        return NoMethodCollisionsDict()

    def __new__(metacls, name, bases, namespace):
        return super().__new__(metacls, name, bases, namespace)


class NoMethodCollisions(metaclass=NoMethodCollisionsMetaClass):
    pass
