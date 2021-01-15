# MutableString

This week I'd like you to make a class called `MutableString` which will act like a string, except it will be mutable.

Aside: if you didn't know, strings in Python are immutable, meaning no matter how hard you might try to change 
them you can't. All string operations return a new string object instead of mutating the one you already have.

So `MutableString` should work like this:

    >>> greeting = MutableString("Hello world!")
    >>> greeting
    'Hello world!'
    >>> greeting[4] = "a"
    >>> greeting
    'Hella world!'

Concatenation, containment checks, and string methods should work on your `MutableString` objects:

    >>> greeting = MutableString("Hello world!")
    >>> greeting.endswith('!')
    True
    >>> greeting + MutableString('!')
    'Hella world!!'
    >>> (greeting + '?').lower()
    'hello world!?'
    >>> 'la' in greeting
    True
    >>> len(greeting)
    12

#### Bonus 1

For the first bonus, I'd like you to make sure that you can assign and delete slices of `MutableString` objects:

    >>> greeting = MutableString("Hello world!")
    >>> greeting[6:-1] = "there"
    >>> greeting
    'Hello there!'
    >>> del greeting[5:-1]
    >>> greeting
    'Hello!'
    >>> del greeting[-1]
    >>> greeting
    'Hello world'

#### Bonus 2

For the second bonus, you should make sure various operations on your class return `MutableString` objects:

    >>> greeting = MutableString("Hello world!")
    >>> exclamation = greeting[-1]
    >>> hello = greeting[:5]
    >>> type(exclamation), type(hello)
    (<class 'MutableString'>, <class 'MutableString'>)
    >>> double_exclamation = exclamation + "!"
    >>> lowercased_hello = hello.lower()
    >>> type(double_exclamation), type(lowercased_hello)
    (<class 'MutableString'>, <class 'MutableString'>)
    >>> characters = list(double_exclamation)
    >>> [type(c) for c in characters]
    [<class 'MutableString'>, <class 'MutableString'>]

#### Bonus 3

For the third bonus, you should make sure that methods typically found on mutable sequences (`append`, `insert`, 
and `pop`) work on your `MutableString` objects:

    >>> greeting = MutableString("Hello world")
    >>> greeting.append("!")
    >>> greeting
    'Hello world!'
    >>> greeting.insert(5, "o")
    >>> greeting
    'Helloo world!'
    >>> greeting.pop(5)
    >>> greeting
    'Hello world!'
    >>> greeting.pop()
    'Hello world'
