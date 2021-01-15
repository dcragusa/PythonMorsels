
class Unsubclassable:
    def __init_subclass__(cls, **kwargs):
        raise TypeError('Unacceptable base type')


def prevent_subclassing():
    raise TypeError('Unacceptable base type')


def final_class(cls):
    setattr(cls, '__init_subclass__', prevent_subclassing)
    return cls


class UnsubclassableType(type):
    def __new__(cls, name, bases, dct):
        c = super().__new__(cls, name, bases, dct)
        setattr(c, '__init_subclass__', prevent_subclassing)
        return c

