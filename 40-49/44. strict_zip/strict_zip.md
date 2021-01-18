# strict_zip

This week you have to write a `strict_zip` function, which acts like the built-in `zip` function except that 
looping over sequences with different lengths should raise an exception.

Your `strict_zip` function should accept zero or more sequences and should return an iterable of tuples, 
just like the `zip` function does.

    >>> for number, letter in strict_zip((1, 2, 3), 'abc'):
        ...     print(number, letter)
    ...
    1 a
    2 b
    3 c
    >>> for items in strict_zip([1, 2], [3, 4], [5, 6], [7, 8]):
        ...     print(items)
    ...
    (1, 3, 5, 7)
    (2, 4, 6, 8)
    >>> list(strict_zip())
    []

Unlike `zip`, when `strict_zip` is passed a sequence which has different numbers of elements, 
a `ValueError` should be raised.

    >>> for letters in strict_zip('here', 'are', 'four', 'sequences'):
        ...     print(*letters)
    ...
    h a f s
    e r o e
    r e u q
    Traceback (most recent call last):
    File "<stdin>", line 1, in <module>
    File "strict_zip.py", line 11
    ValueError: value out of range

There are three bonuses this week. I recommend attempting the base problem first before attempting any of the bonuses.

#### Bonus 1

In the first bonus, `strict_zip` should take accept all iterables, not just sequences. For this bonus, 
only finite iterables will be passed to `strict_zip`.

    >>> lucas = [2, 1, 3, 4, 7, 11]
    >>> dict(strict_zip(lucas, (n**2 for n in lucas)))
    {2: 4, 1: 1, 3: 9, 4: 16, 7: 49, 11: 121}
    >>> for x, y in strict_zip((n**2 for n in lucas), [1, 2, 3]):
        ...     print(x, y)
    ...
    4 1
    1 2
    9 3
    Traceback (most recent call last):
    File "<stdin>", line 1, in <module>
    File "strict_zip.py", line 11
    ValueError: value out of range

#### Bonus 2

For the second bonus, make sure that your `strict_zip` function returns an iterator.

    >>> lucas = [2, 1, 3, 4, 7, 11]
    >>> zipped = strict_zip(lucas, (n**2 for n in lucas))
    >>> next(zipped)
    (2, 4)
    >>> next(zipped)
    (1, 1)
    >>> list(zipped)
    [(3, 9), (4, 16), (7, 49), (11, 121)]

#### Bonus 3

For the third bonus, `strict_zip` should work with infinitely long iterables, such as `itertools.count` 
and `itertools.repeat`.

    >>> from itertools import repeat, count, islice
    >>> zipped = strict_zip([1, 2, 3], repeat(4))
    >>> next(zipped)
    (1, 4)
    >>> next(zipped)
    (2, 4)
    >>> next(zipped)
    (3, 4)
    >>> next(zipped)
    Traceback (most recent call last):
    File "<stdin>", line 1, in <module>
    File "strict_zip.py", line 34
    ValueError: value out of range
    >>> numbers_with_squares = strict_zip(count(), (n**2 for n in count()))
    >>> list(islice(numbers_with_squares, 7))
    [(0, 0), (1, 1), (2, 4), (3, 9), (4, 16), (5, 25), (6, 36)]
