# PiecewiseRange

This week I'd like you to create a `PiecewiseRange` class which is similar to the `parse_ranges`. This 
`PiecewiseRange` class should accept a range of integers as a string and return a lazy iterable which acts 
similar to Python's `range` objects.

    >>> r = PiecewiseRange('1-2, 4, 8-10, 11')
    >>> list(r)
    [1, 2, 4, 8, 9, 10, 11]

#### Bonus 1

For the first bonus, your `PiecewiseRange` object should work with `len` and you should make sure your 
`PiecewiseRange` objects are not iterators (after all, `range` is not an iterator).

    >>> r = PiecewiseRange('1-2, 4, 8-10, 11')
    >>> len(r)
    7
    >>> next(r)
    Traceback (most recent call last):
    File "<stdin>", line 1, in <module>
    TypeError: 'PiecewiseRange' object is not an iterator

#### Bonus 2

For the second bonus, your `PiecewiseRange` objects should be indexable:

    >>> r = PiecewiseRange('1-2, 4, 8-10, 11')
    >>> r[1]
    2
    >>> r[4]
    9

#### Bonus 3

For third bonus, equivalent `PiecewiseRange` objects should have the same string representation and should be seen 
as equal to each other:

    >>> PiecewiseRange('1-2,3,4,11')
    PiecewiseRange('1-4,11')
    >>> PiecewiseRange('1-2,3,4,11') == PiecewiseRange('1-4,11')
    True
    >>> PiecewiseRange('1-2,3,4,11') == PiecewiseRange('1-4,13')
    False
