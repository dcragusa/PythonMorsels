
class computed_property:

    def __init__(self, *args):
        self.attributes = list(args)
        self._getter = self._setter = None
        self.name = None

    def __call__(self, func):
        self._getter = func
        return self

    def __get__(self, instance, class_=None):
        if instance is None:
            return self
        current_attr_vals = {attr: getattr(instance, attr, None) for attr in self.attributes}
        # we have to use the instance dict, as non-hashable descriptors cannot be used in a weak key dict
        if self.name not in instance.__dict__ or current_attr_vals != instance.__dict__[self.name]['attr_vals']:
            instance.__dict__[self.name] = {'attr_vals': current_attr_vals, 'property_val': self._getter(instance)}
        return instance.__dict__[self.name]['property_val']

    def setter(self, setter):
        self._setter = setter
        return self

    def __set__(self, instance, value):
        if self._setter is not None:
            self._setter(instance, value)
        else:
            raise AttributeError("Can't set attribute")

    def __set_name__(self, instance, name):
        self.name = name
