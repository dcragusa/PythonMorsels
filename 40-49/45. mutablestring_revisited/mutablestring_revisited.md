# MutableString Revisited

This week I'd like you to revisit the `MutableString` class we've already made.

The base tests this week are quite a bit more challenging than they were for the first `MutableString` problem.

    >>> greeting1 = MutableString("hey")
    >>> greeting2 = hey[:2]
    >>> greeting2.extend("llo")
    >>> greeting2
    'hello'
    >>> greeting1[1:] = "i there"
    >>> greeting1
    'hi there'
    >>> popped = greeting1.pop()
    >>> greeting1
    'hi ther'
    >>> type(popped)
    <class 'mutablestring2.MutableString'>

Your `MutableString` should have all the functionality of a mutable sequence and each of the strings returned from 
your `MutableString` (by indexing, slicing, popping, etc.) should also be `MutableString` instances.

#### Bonus 1

For the first bonus, I'd like you to make sure in-place addition does in fact mutate in-place:

    >>> greeting1 = MutableString("hey")
    >>> greeting2 = greeting1
    >>> greeting2 += "!! "
    >>> greeting1
    'hey!! '
    >>> greeting1 *= 2
    >>> greeting2
    'hey!! hey!!'

#### Bonus 2

For the second bonus, I'd like you to make sure your `MutableString` class includes the various methods you'd 
expect a string to have:

    >>> greeting1 = MutableString("hey")
    >>> greeting2 = greeting1.replace('e', 'i').title()
    >>> greeting2.append("a!")
    >>> greeting2
    'Hiya!'
    >>> greeting2.endswith('!')
    True

#### Bonus 3

For the third bonus, I'd like you to make sure your `MutableString` can actually be used anywhere a string 
would normally be used. For example, the string `join` method should accept `MutableString` objects:

    >>> greetings = [MutableString(x) for x in ("hi", "hey", "hello")]
    >>> ", ".join(greetings)
    'hi, hey, hello'
