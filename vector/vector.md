# Vector

This week I'd like you to make a 3-dimensional Vector class which that works with multiple assignment, supports equality and inequality operators.

    >>> v = Vector(1, 2, 3)
    >>> x, y, z = v
    >>> print(x, y, z)
    1 2 3
    >>> v == Vector(1, 2, 4)
    False
    >>> v == Vector(1, 2, 3)
    True

The Vector class also must use __slots__ for efficient attribute lookups, meaning other attributes won't be able to be assigned to it and it won't have a __dict__ like most classes we make do.

    >>> v.a = 4
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
    AttributeError: 'Vector' object has no attribute 'a'
    >>> v.__dict__
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
    AttributeError: 'Vector' object has no attribute '__dict__'

The tests also check to make sure your Vector class doesn't support odd behavior that it shouldn't have (like support for < and >).

I recommend solving the main problem before attempting the bonuses. If you finish quickly, try some of the bonuses.

#### Bonus 1

For the first bonus, I'd like you to make your Vector objects support addition and subtraction with other Vector objects:

    >>> Vector(1, 2, 3) + Vector(4, 5, 6) == Vector(5, 7, 9)
    True
    >>> Vector(5, 7, 9) - Vector(3, 1, 2) == Vector(2, 6, 7)
    True

Note that addition and subtraction shouldn't work in-place: they should return a new Vector object.

#### Bonus 2

For the second bonus, I'd like your vector to support multiplication and division by numbers (this should return a new scaled vector):

    >>> 3 * Vector(1, 2, 3) == Vector(3, 6, 9)
    True
    >>> Vector(1, 2, 3) * 2 == Vector(2, 4, 6)
    True
    >>> Vector(1, 2, 3) / 2 == Vector(0.5, 1, 1.5)
    True

#### Bonus 3

For the third bonus, I'd like you to make your Vector class immutable, meaning the coordinates (x, y, and z) cannot be changed after a new Vector has been defined:

    >>> v = Vector(1, 2, 3)
    >>> v.x = 4
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
        raise AttributeError("Vectors are immutable")
    AttributeError: Vectors are immutable
