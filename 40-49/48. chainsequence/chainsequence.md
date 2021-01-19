# ChainSequence

This week I'd like you to write a `ChainSequence` class which chains together a number of sequences. 
This class will be sort of like `collections.ChainMap`, but for sequences instead of "mappings".

For example:

    >>> chained = ChainSequence('abcd', [1, 2, 3])
    >>> chained[1]
    'b'
    >>> chained[-1]
    3
    >>> chained[4]
    1
    >>> len(chained)
    7

Your `ChainSequence` objects should be indexable, should have a length, and should be iterable (and can be 
iterated over multiple times).

Your `ChainSequence` should also have a `sequences` attribute which contains the sequences it wraps around. 
If one of these sequences changes, it should change also.

    >>> x = [2, 1]
    >>> y = [3, 4]
    >>> z = [11, 18]
    >>> chained = ChainSequence(x, y, z)
    >>> chained.sequences
    [[2, 1], [3, 4], [11, 18]]
    >>> len(chained)
    6
    >>> chained[4], chained[5]
    (11, 18)
    >>> y.append(7)
    >>> chained[4], chained[5]
    (7, 11)
    >>> len(chained)
    7

#### Bonus 1

For the first bonus I'd like your `ChainSequence` objects to be sliceable. Slicing a `ChainSequence` 
should return a `SliceView` object (remember `SliceView`?).

    >>> chained = ChainSequence('abcd', [1, 2, 3])
    >>> tuple(chained[3:])
    ('d', 1, 2, 3)
    >>> chained.sequences[-1][0] = 9
    >>> tuple(chained[3:6])
    ('d', 9, 2)

#### Bonus 2

For the second bonus, I'd like you to implement a nice string representation to your `ChainSequence` objects.

    >>> chained = ChainSequence('abcd', [1, 2, 3])
    >>> chained
    ChainSequence('abcd', [1, 2, 3])
    >>> chained.sequences[-1][0] = 9
    ChainSequence('abcd', [9, 2, 3])

#### Bonus 3

For the third bonus, make your `ChainSequence` objects support `+` and `+=` with other sequences. The `+` 
operator should return a new `ChainSequence` object. The `+=` operator should mutate the `ChainSequence` object.

    >>> chained = ChainSequence('abcd', [1, 2, 3])
    >>> chained + 'hello'
    ChainSequence('abcd', [1, 2, 3], 'hello')
    >>> chained += (4,5, 6)
    >>> chained
    ChainSequence('abcd', [1, 2, 3], (4, 5, 6))
