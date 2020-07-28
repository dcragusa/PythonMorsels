# SequenceZip

This week I'd like you to create a class, `SequenceZip`, which acts sort of like the built-in `zip` class, but special-purposed for zipping sequences together (sequences are list-like things that have a length and indexes).

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

In addition, these `SequenceZip` objects should have a length (the length of the shortest sequence) and they should be indexable:

    >>> len(zipped)
    3
    >>> zipped[1]
    ('B', 'easy', 2)

Your `SequenceZip` object is only expected to work with sequences (like lists and strings). Your `SequenceZip` objects shouldn't copy the sequences given to them.

The base problem is an interesting enough collection on its own, but if you'd like to add some extra features to your `SequenceZip` class try the bonuses out.

#### Bonus 1

For the first bonus, I'd like your `SequenceZip` objects to have a nice string representation:

    >>> zipped = SequenceZip('ABC', ['as', 'easy', 'as'], [1, 2, 3])
    >>> zipped
    SequenceZip('ABC', ['as', 'easy', 'as'], [1, 2, 3])
    >>> SequenceZip(range(10), "hello")
    SequenceZip(range(0, 10), 'hello')

#### Bonus 2

For the second bonus, I'd like your `SequenceZip` class to support equality, meaning you can ask two different `SequenceZip` objects if they contain the same items:

    >>> SequenceZip('hiya', [1, 2]) == SequenceZip('hi', [1, 2, 3])
    True
    >>> SequenceZip('hiya', [1, 2, 3]) == SequenceZip('hi', [1, 2, 3])
    False

Equality shouldn't loop over every item in all sequences but should delegate equality to the sequences themselves. This can improve performance with some objects (like range objects).

#### Bonus 3

For the third bonus, I'd like your `SequenceZip` objects to support slicing:

    >>> zipped = SequenceZip('ABCDE', [1, 2, 3, 4, 5])
    >>> zipped[1:]
    SequenceZip('BCDE', [2, 3, 4, 5])

The third bonus will likely be a bit trickier than the other two.
