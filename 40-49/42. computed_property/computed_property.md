# computed_property

This week I'd like you to create a `computed_property` decorator that is somewhat similar to the `property` 
decorator (and the `cached_property` decorator you've already made).

The `computed_property` decorator should accept an attribute name and cache the value of the property as long 
as that attribute's value remains the same.

    class Circle:
        def __init__(self, radius=1):
            self.radius = radius
        @computed_property('radius')
        def diameter(self):
            print('computing diameter')
            return self.radius * 2
    
    >>> circle = Circle()
    >>> circle.diameter
    computing diameter
    2
    >>> circle.diameter
    2
    >>> circle.radius = 3
    >>> circle.diameter
    computing diameter
    6

Just like the `property` decorator, `computed_property` instances should be unsettable and should be accessible 
on classes:

    >>> circle.diameter = 4
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
    AttributeError: can't set attribute
    >>> Circle.diameter
    <__main__.computed_property object at 0x7fe427c6c8d0>

#### Bonus 1

For the first bonus, allow your `computed_property` decorator to accept multiple attributes on which it depends:

    from math import sqrt
    class Vector:
        def __init__(self, x, y, z, color=None):
            self.x, self.y, self.z = x, y, z
            self.color = color
        @computed_property('x', 'y', 'z')
        def magnitude(self):
            print('computing magnitude')
            return sqrt(self.x**2 + self.y**2 + self.z**2)
    
    >>> v = Vector(9, 2, 6)
    >>> v.magnitude
    computing magnitude
    11.0
    >>> v.color = 'red'
    >>> v.magnitude
    11.0
    >>> v.y = 18
    >>> v.magnitude
    computing magnitude
    21.0

#### Bonus 2

For the second bonus, make sure non-existent attribute dependencies are allowed:

    class Circle:
        def __init__(self, radius=1):
            self.radius = radius
        @computed_property('radius', 'area')
        def diameter(self):
            return self.radius * 2

Non-existent attributes should be ignored. As long as an attribute is missing, it should be treated as unchanging.

    >>> circle = Circle()
    >>> circle.diameter
    2

#### Bonus 3

For the third bonus, allow your `computed_property` to have a setter method:

    class Circle:
        def __init__(self, radius=1):
            self.radius = radius
        @computed_property('radius')
        def diameter(self):
            return self.radius * 2
        @diameter.setter
        def diameter(self, diameter):
            self.radius = diameter / 2

The `computed_property` setter method should work just like the `property` setter method:

    >>> circle = Circle()
    >>> circle.diameter
    2
    >>> circle.diameter = 3
    >>> circle.radius
    1.5
