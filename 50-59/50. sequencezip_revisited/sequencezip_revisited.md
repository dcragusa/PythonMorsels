# SequenceZip Revisited

This week I'd like you to revisit the `SequenceZip` class you've already made.

This class acted like `zip`, but it's special-purposed for zipping sequences (like-like things) together.

    >>> zipped = SequenceZip('ABC', ['as', 'easy', 'as'], [1, 2, 3])
    >>> for x, y, z in zipped:
    ...     print(x, y, z)
    ...
    A as 1
    B easy 2
    C as 3
    >>> list(zipped)
    [('A', 'as', 1), ('B', 'easy', 2), ('C', 'as', 3)]

Notice that this `SequenceZip` class works kind of like `zip` except you can loop over it multiple times.

In addition, these `SequenceZip` objects should have a length (the length of the shortest sequence) and they 
should be indexable:

    >>> len(zipped)
    3
    >>> zipped[1]
    ('B', 'easy', 2)

And `SequenceZip` objects should be comparable to each other with the `==` and `!=` operators:

    >>> SequenceZip('hiya', [1, 2]) == SequenceZip('hi', [1, 2, 3])
    True
    >>> SequenceZip('hiya', [1, 2, 3]) == SequenceZip('hi', [1, 2, 3])
    False

This `SequenceZip` class is only expected to work with sequences (like lists and strings). `SequenceZip` objects 
shouldn't copy the sequences given to them. You can solve the base problem by copy-pasting a solution to bonus 2 
from the original `SequenceZip` problem. I recommend attempting to re-solve this without relying on your code 
from before first. The bonuses might feel a bit contrived this time, but I hope you'll have fun with the challenge
of adding new features to this class.

#### Bonus 1

For the first bonus, I'd like your SequenceZip objects to support slicing:

    >>> zipped = SequenceZip('ABCDE', [1, 2, 3, 4, 5])
    >>> zipped[1:]
    SequenceZip('BCDE', [2, 3, 4, 5])

#### Bonus 2

For the second bonus, I'd like your `SequenceZip` class to be mutable. `SequenceZip` objects should support 
assignment to indexes and deleting of items based on their index.

    >>> zipped = SequenceZip([0, 1, 2], [3, 4, 5, 6])
    >>> zipped[0] = [8, 9]
    >>> zipped
    SequenceZip([8, 1, 2], [9, 4, 5, 6])
    >>> del zipped[-1]
    >>> zipped
    SequenceZip([8, 1], [9, 4, 6])

When assigning into a `SequenceZip` object, a sequence of the correct length (the number of sequences being wrapped 
around) must be provided. Note that mutating `SequenceZip` objects will fail if they wrap around immutable sequences.

    >>> zipped = SequenceZip('ABCDE', [1, 2, 3, 4, 5])
    >>> del zipped[0]
    Traceback (most recent call last):
    File "<stdin>", line 1, in <module>
    File "<stdin>", line 32, in __delitem__
    TypeError: 'str' object doesn't support item deletion

#### Bonus 3

For the third bonus I'd like your `SequenceZip` objects to support append and insert operations as well.

    >>> zipped = SequenceZip([0, 1, 2], [3, 4, 5, 6])
    >>> zipped.append((7, 8))
    >>> zipped
    SequenceZip([0, 1, 2, 7], [3, 4, 5, 8])
    >>> zipped.insert(0, (9, 10))
    >>> zipped
    SequenceZip([9, 0, 1, 2, 7], [10, 3, 4, 5, 8, 6])

Notice that append doesn't insert if an existing item can be updated instead.
