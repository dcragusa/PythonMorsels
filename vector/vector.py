from numbers import Number

class Vector:
    __slots__ = ['x', 'y', 'z']

    def __init__(self, x, y, z):
        self.x, self.y, self.z = x, y, z

    def __iter__(self):
        yield self.x
        yield self.y
        yield self.z

    def __eq__(self, other):
        if not isinstance(other, Vector):
            return NotImplemented
        return tuple(self) == tuple(other)

    def __add__(self, other):
        if not isinstance(other, Vector):
            return NotImplemented
        return Vector(self.x + other.x, self.y + other.y, self.z + other.z)

    def __sub__(self, other):
        if not isinstance(other, Vector):
            return NotImplemented
        return Vector(self.x - other.x, self.y - other.y, self.z - other.z)

    def __mul__(self, other):
        if not isinstance(other, Number):
            return NotImplemented
        return Vector(self.x * other, self.y * other, self.z * other)

    def __rmul__(self, other):
        return self.__mul__(other)

    def __truediv__(self, other):
        if not isinstance(other, Number):
            return NotImplemented
        return Vector(self.x / other, self.y / other, self.z / other)

    def __setattr__(self, key, value):
        if hasattr(self, key):
            # we can check for any keys as we are only supposed to have xyz anyways
            raise AttributeError('Vectors are immutable')
        super().__setattr__(key, value)
