# validators

This week I'd like you to make a descriptor that validates that the value it's assigned to is a positive number. 
If you've never made a descriptor before, you'll need to look up how to do that.

Your descriptor, `PositiveNumber`, should work like this:

    >>> class Point:
    ...     x = PositiveNumber(1)
    ...     y = PositiveNumber(1)
    ...     z = PositiveNumber(1)
    ...
    >>> p = Point()
    >>> p.x = 4
    >>> p.x
    4
    >>> p.x = -3
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
      File "<stdin>", line 9, in __set__
    ValueError: Positive number required.
    >>> (p.x, p.y, p.z)
    (4, 1, 1)

The descriptor will accept an initial value and will raise an exception if assigned to anything besides a number 
which is greater than zero.

#### Bonus 1

For the first bonus, I'd like you to make the initial value optional and I'd like you to make sure your 
`PositiveNumber` class doesn't leak memory (if `Point` objects are created and deleted in the code below, they 
shouldn't stick around in memory).

    >>> class Point:
    ...     x = PositiveNumber()
    ...     y = PositiveNumber()
    ...     z = PositiveNumber()
    ...
    >>> p = Point()
    >>> p.x = 4
    >>> p.x
    4
    >>> p.y
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
      File "<stdin>", line 7, in __get__
    AttributeError: 'Point' object has no attribute 'y'

An `AttributeError` should be raised if the attribute hasn't been assigned a value yet. The error message for the 
`AttributeError` should be helpful if possible (you may find it tricky to display the particular error message above 
though).

#### Bonus 2

For the second bonus, I'd like you to create a new `Validator` base class which `PositiveNumber` should inherit from. 
This `Validator` class should create descriptors from child classes, which will need a `validate` method.

Here's an example descriptor:

    class Choice(Validator):
        def __init__(self, *choices):
            super().__init__()
            self.choices = choices
        def validate(self, value):
            if value not in self.choices:
                raise ValueError(f"Must be one of: {', '.join(self.choices)}")

And an example usage:

    >>> class Point:
    ...     x = PositiveNumber()
    ...     y = PositiveNumber()
    ...     z = PositiveNumber()
    ...     color = Choice('red', 'blue', 'green')
    ...
    >>> p = Point()
    >>> p.color = 'red'
    >>> p.color
    'red'
    >>> p.color = 'grue'
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
      File "<stdin>", line 13, in __set__
      File "<stdin>", line 6, in validate
    ValueError: Must be one of: red, blue, green

#### Bonus 3

For the third bonus, make sure your `Validator` class returns a `TypeError` when attempting to initialize a subclass 
that doesn't have a `validate` method:

    >>> class X(Validator): pass
    ...
    >>> class Thing:
    ...     x = X()
    ...
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
      File "<stdin>", line 2, in Thing
    TypeError: Can't instantiate abstract class X with abstract methods validate

The error message displayed above should be a hint as to how you might do that.
