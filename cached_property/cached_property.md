# cached_property

This week I'd like you to create a `cached_property` decorator that is somewhat similar to the `property` decorator.

A cached property should compute its value once, the first time it's accessed. After that the cached property should always return the previously cached value.

    from collections import namedtuple
    
    class Circle(namedtuple('BaseCircle', ['radius'])):
        @cached_property
        def diameter(self):
            return self.radius * 2

The cached property value should be able to be overridden by assignment (unlike `property`).

    >>> c = Circle(5)
    >>> c.diameter
    10
    >>> c.diameter = 20
    >>> c.diameter
    20
    >>> c.radius
    5

#### Bonus 1

For the first bonus, you should allow the cache (or overridden value) to be cleared by using the `del` statement on your cached property:

    >>> from math import sqrt
    >>> class RightTriangle:
    ...     def __init__(self, a, b):
    ...         self.a, self.b = a, b
    ...     @cached_property
    ...     def c(self):
    ...         return sqrt(self.a**2 + self.b**2)
    ...
    >>> t = RightTriangle(3, 4)
    >>> t.c
    5.0
    >>> t.b = 2
    >>> t.c
    5.0
    >>> del t.c
    >>> t.c
    3.605551275463989
    >>> t.c = 10
    >>> t.b = 4
    >>> t.c
    10
    >>> del t.c
    >>> t.c
    5.0

#### Bonus 2

For the second bonus, I'd like you to make sure accessing your `cached_property` instances from classes works (property works this way too):

    >>> t = RightTriangle(3, 4)
    >>> RightTriangle.c
    <__main__.cached_property object at 0x7f59c1e4b7f0>
    >>> RightTriangle.c.__get__(t)
    5.0

#### Bonus 3

For the third bonus, I'd like you to allow users of `cached_property` to hook into the setting and deleting features using a syntax similar to the one `property` supports:

    class Circle:
        def __init__(self, radius=1):
            self.radius = radius
        @cached_property
        def diameter(self):
            return self.radius * 2
        @diameter.setter
        def diameter(self, diameter):
            if diameter < 0:
                raise ValueError("Must be positive")
            self.radius = diameter / 2
        @diameter.deleter
        def diameter(self):
            print('Cached diameter value cleared')

This new class would work like this:

    >>> c = Circle(5)
    >>> c.diameter
    8
    >>> c.diameter = 16
    >>> c.radius
    8.0
    >>> c.diameter
    16.0
    >>> c.radius = 4
    >>> c.diameter
    16.0
    >>> del c.diameter
    Cached diameter value cleared
    >>> c.diameter
    8
