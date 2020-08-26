# final_class

This week I'd like you to do something which might sound odd, but it should be informative: I'd like you to work on 
making classes which cannot be subclassed.

If you try to subclass `bool` or `NoneType` (`type(None)`) you'll get an error:

    >>> class MyNone(type(None)): pass
    ...
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
    TypeError: type 'NoneType' is not an acceptable base type

I'd like you to make a class, called `Unsubclassable`, that also doesn't allow subclassing.

At first you only need to make a class whose subclasses cannot be constructed.

    >>> class MyClass(Unsubclassable):
    ...     def __init__(self, x):
    ...         self.x = x
    ...
    >>> MyClass()
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
    TypeError: type 'Unsubclassable' is not an acceptable base type

A `TypeError` should be raised, but it doesn't matter what the message in the type error is (though more helpful is 
better).

#### Bonus 1

For a bit more of a challenge, make your `Unsubclassable` class raise an exception at the time it is subclassed.

    >>> class MyClass(Unsubclassable):
    ...     def __init__(self, x):
    ...         self.x = x
    ...
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
    TypeError: Unacceptable base type

Again it doesn't matter what the error message is in the raised `TypeError`.

#### Bonus 2

This bonus is where we start making something fun and possibly useful (though probably not directly, since this 
example is odd).

I'd like you to make a class decorator called `final_class` which will make the decorated class unsubclassable.

Here's an example of using `final_class`:

    >>> @final_class
    ... class Base:
    ...     pass
    ...

And here's an example of the exception we might see when subclassing this new "final" class:

    >>> class MyClass(Base):
    ...     pass
    ...
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
    TypeError: Unacceptable base type

#### Bonus 3

This bonus is actually a bit of a hint for the prior two bonuses.

If you haven't already done so, I'd like you to create a metaclass called `UnsubclassableType` which will make its 
classes unsubclassable.

    >>> class Base(metaclass=UnsubclassableType):
    ...     pass
    ...
    >>> class MyClass(Base): pass
    ...
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
    TypeError: Unacceptable base type
