from abc import ABC, abstractmethod
from weakref import WeakKeyDictionary

MISSING = object()


# class PositiveNumber:
#
#     def __init__(self, default=MISSING):
#         self.default = default
#         self.data = WeakKeyDictionary()
#         self.class_name_map = WeakKeyDictionary()
#
#     def __set_name__(self, owner, name):
#         self.class_name_map[owner] = name
#
#     def __get__(self, obj, objtype):
#         if obj in self.data:
#             return self.data[obj]
#         elif self.default is not MISSING:
#             return self.default
#         else:
#             raise AttributeError(f"'{objtype.__name__}' object has no attribute '{self.class_name_map[objtype]}'")
#
#     def __set__(self, obj, val):
#         if val <= 0:
#             raise ValueError('Positive number required.')
#         self.data[obj] = val


class Validator(ABC):

    def __init__(self, default=MISSING):
        self.default = default
        self.data = WeakKeyDictionary()
        self.class_name_map = WeakKeyDictionary()

    def __set_name__(self, owner, name):
        self.class_name_map[owner] = name

    def __get__(self, obj, objtype):
        if obj in self.data:
            return self.data[obj]
        elif self.default is not MISSING:
            return self.default
        else:
            raise AttributeError(f"'{objtype.__name__}' object has no attribute '{self.class_name_map[objtype]}'")

    def __set__(self, obj, val):
        self.validate(val)
        self.data[obj] = val

    @abstractmethod
    def validate(self, val):
        return NotImplementedError


class PositiveNumber(Validator):
    def validate(self, val):
        if val <= 0:
            raise ValueError('Positive number required.')
