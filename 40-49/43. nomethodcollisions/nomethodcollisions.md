# NoMethodCollisions

This week I'd like you to create a class that catches a specific Python bug. This is a `NoMethodCollisions` 
class which, when inherited from, will disallow the same method name from being defined twice.

Your class should raise an error for a class like this:

    from unittest import TestCase
    from classtools import NoMethodCollisions
    
    class BasicTests(NoMethodCollisions, TestCase):
        def test_adding(self):
            assert 2 + 2 == 4
        def test_subtracting(self):
            assert 4 - 2 == 2
        def test_adding(self):
            assert 1 + 1 == 2

The error should happen when the class is defined. The redefinition of methods decorated by `classmethod` 
or `staticmethod` should also result in an error. This is a pretty tricky problem, so don't be discouraged 
if you need to check the hints.

#### Bonus 1

For the first bonus, I'd like you to make sure the exception that is raised is a TypeError.

    >>> class BasicTests(NoMethodCollisions):
    ...     def test_adding(self):
    ...         assert 2 + 2 == 4
    ...     def test_subtracting(self):
    ...         assert 4 - 2 == 2
    ...     def test_adding(self):
    ...         assert 1 + 1 == 2
    ...
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
      File "<stdin>", line 6, in BasicTests
      File "<stdin>", line 5, in __setitem__
    TypeError: test_adding already defined in class.

#### Bonus 2

For the second bonus, I'd like you to make sure that properties (made with `@property`) work properly, 
even when they have setter methods:

So this class should not raise an exception:

    class Circle(NoMethodCollisions):
        def __init__(self, radius=1):
            self.radius = radius
        @property
        def diameter(self):
            return self.radius * 2
        @diameter.setter
        def diameter(self, diameter):
            self.radius = diameter / 2

#### Bonus 3

For the third bonus, make sure your class only checks for method collisions on callables and descriptors 
(like `classmethod` and `staticmethod`).

    >>> class Namespace(NoMethodCollisions):
    ...     total = 1
    ...     for x in range(2, 10):
    ...         total *= x
    ...
    >>> Namespace.total
    362880
    >>> Namespace.x
    9
