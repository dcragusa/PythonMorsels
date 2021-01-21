# RomanNumeral

This week I'd like you to make a class which represents a Roman numeral. This might seem a bit silly, but we'll 
see a few interesting Python class features along the way.

At first, I'd like your `RomanNumeral` class to accept a Roman numeral string and to support conversion to an integer:

    >>> four = RomanNumeral('IV')
    >>> int(four)
    4

You don't need a friendly string representation at first and you don't need to handle converting Roman numerals 
from numbers:

    >>> five = RomanNumeral('V')
    <__main__.RomanNumeral at 0x7f65007b67b8>

#### Bonus 1

For the first bonus, I'd like you to make a nice string representation for your `RomanNumeral` class and add a 
`from_int` factory method on your `RomanNumeral` class which will create a Roman numeral from an integer.

    >>> nine = RomanNumeral('IX')
    >>> nine
    RomanNumeral('IX')
    >>> nineteen_ninety_nine = RomanNumeral.from_int(1999)
    >>> str(nineteen_ninety_nine)
    'MCMXCIX'
    >>> print(nineteen_ninety_nine)
    MCMXCIX

#### Bonus 2

For the second bonus, I'd like you to make your `RomanNumeral` class support addition with both integers and 
other `RomanNumeral` objects.

    >>> RomanNumeral('XI') + RomanNumeral('II')
    RomanNumeral('XIII')
    >>> RomanNumeral('XI') + RomanNumeral('III')
    RomanNumeral('XIV')
    >>> RomanNumeral('IIII') + 12
    RomanNumeral('XVI')

#### Bonus 3

For the third bonus, I'd like you to implement equality and ordering for RomanNumeral objects.

The rules for this are that:
- RomanNumeral objects should be comparable to other RomanNumeral objects 
- RomanNumeral objects should be comparable to numbers 
- RomanNumeral objects can be compared using equality/inequality to strings, but cannot be ordered with strings
```
>>> fourteen = RomanNumeral('XIV')
>>> fourteen2 = RomanNumeral('XIIII')
>>> fifteen = RomanNumeral('XV')
>>> fourteen == fourteen2
True
>>> fourteen == fifteen
False
>>> fourteen < fifteen
True
>>> fourteen > fifteen
False
>>> fourteen <= fifteen
True
>>> fourteen == "XIV"
True
>>> fourteen < "XIV"
>>> RomanNumeral('XIV') < "XIV"
Traceback (most recent call last):
File "<stdin>", line 1, in <module>
TypeError: '<' not supported between instances of 'RomanNumeral' and 'str'
```
