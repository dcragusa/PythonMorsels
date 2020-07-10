# Unpacker 

This week I'd like you to create an `Unpacker` class which (optionally) accepts an ordered dictionary as argument. The given dictionary items should be retrievable and settable using either an attribute or a key syntax on the `Unpacker` object.

    >>> d = {'hello': 4, 'hi': 5}
    >>> u = Unpacker(d)
    >>> u['hello']
    4
    >>> u.hi
    5
    >>> u['hello'] = 8
    >>> u.hello
    8

You can assume that the given dictionary keys will be strings which represent valid attribute names.

I'd like attribute assignment on your object to work as expected:

    >>> u.hello = 5
    >>> u.hello
    5

#### Bonus 1

For the first bonus, I'd like you to make sure your `Unpacker` objects can be "unpacked" using with multiple assignment. The unpacking should be in the order of assignment (assuming the given dictionary is ordered).

    >>> from collections import OrderedDict
    >>> coordinates = OrderedDict([('x', 34), ('y', 67)])
    >>> point = Unpacker(coordinates)
    >>> x_axis, y_axis = point
    >>> x_axis, y_axis
    (34, 67)

#### Bonus 2

For the second bonus I'd like you to make a nice string representation for your `Unpacker` objects.

    >>> row = Unpacker({'a': 234, 'b': 54})
    >>> row['a'] = 11
    >>> row['c'] = 45
    >>> row
    Unpacker(a=11, b=54, c=45)

#### Bonus 3

For the third bonus I'd like you to allow getting and setting of multiple attributes using this key-lookup syntax:

    >>> row = Unpacker({'a': 234, 'b': 54})
    >>> row['a', 'b']
    (234, 54)
    >>> row['b', 'a'] = (11, 22)
    >>> row
    Unpacker(a=22, b=11)

In case any one attribute doesn't exist, a `KeyError` exception should be raised:

    >>> row = Unpacker({'a': 234, 'b': 54})
    >>> row['a', 'c', 'b']
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
    KeyError: 'c'
