# FuzzyString

This week I'd like you to write a `FuzzyString` class which acts like a string, but does comparisons in a 
case-insensitive way.

For example:

    >>> greeting = FuzzyString('Hey TREY!')
    >>> greeting == 'hey Trey!'
    True
    >>> greeting == 'heyTrey'
    False
    >>> greeting
    'Hey TREY!'

I'd like you to make sure equality and inequality match case-insensitively at first. I'd also like you to ensure 
that the string representations of your class match Python's string objects' default string representations.

For the first bonus, try to ensure the other comparison operators work as expected:

#### Bonus 1

    >>> o_word = FuzzyString('Octothorpe')
    >>> 'hashtag' < o_word
    True
    >>> 'hashtag' > o_word
    False

#### Bonus 2

For the second bonus, ensure your `FuzzyString` class works with string concatenation and the `in` operator:

    >>> o_word = FuzzyString('Octothorpe')
    >>> 'OCTO' in o_word
    True
    >>> new_string = o_word + ' (aka hashtag)'
    >>> new_string == 'octothorpe (AKA hashtag)'
    True

#### Bonus 3

For the third bonus, also make your string normalize unicode characters when checking for equality:

    >>> ss = FuzzyString('ss')
    >>> '\u00df' == ss
    True
    >>> e = FuzzyString('\u00e9')
    >>> '\u0065\u0301' == e
    True
    >>> '\u0301' in e
    True
