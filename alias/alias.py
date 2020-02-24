
# def alias(alias_var):
#
#     @property
#     def func(cls):
#         return getattr(cls, alias_var)
#
#     return func

# we get bonus 1 for free!

# def alias(alias_var, write=False):
#
#     def getter(cls):
#         return getattr(cls, alias_var)
#
#     def setter(cls, value):
#         if write is True:
#             setattr(cls, alias_var, value)
#         else:
#             raise AttributeError("can't set attribute")
#
#     return property(getter, setter)


class Alias:

    def __init__(self, alias_var, write=False):
        self.alias_var, self.write = alias_var, write

    def __get__(self, instance, owner):
        if instance is None:
            return getattr(owner, self.alias_var)
        else:
            return getattr(instance, self.alias_var)

    def __set__(self, instance, value):
        if self.write is True:
            setattr(instance, self.alias_var, value)
        else:
            raise AttributeError("can't set attribute")


alias = Alias
