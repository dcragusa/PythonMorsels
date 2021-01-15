# parse_ranges

This week I'd like you to write a function called `parse_ranges`, which accepts a string containing ranges of 
numbers and returns an iterable of those numbers.

The numeric ranges in the string will consist of two numbers separated by hyphens and each of the ranges will be 
separated by commas and any number of spaces.

Your function should work like this:

    >>> parse_ranges('1-2,4-4,8-10')
    [1, 2, 4, 8, 9, 10]
    >>> parse_ranges('0-0, 4-8, 20-20, 43-45')
    [0, 4, 5, 6, 7, 8, 20, 43, 44, 45]

In the examples above the functions return lists of numbers. Your function can return any iterable of numbers that 
you'd like though.

If you finish the main problem, try to solve at least one of the bonuses.

#### Bonus 1

For the first bonus, I'd like you to return an iterator (like a generator, not a list) from your function.

You could make a generator function to do this or you could return a generator expression.

    >>> numbers = parse_ranges('100-10000')
    >>> next(numbers)
    100
    >>> next(numbers)
    101

#### Bonus 2

For the second bonus, I'd like you to allow individual numbers as well as pairs of two numbers:

    >>> list(parse_ranges('0,4-8,20,43-45'))
    [0, 4, 5, 6, 7, 8, 20, 43, 44, 45]

#### Bonus 3

For the third bonus I'd like you to do something a bit odd: handle `coverage.py` output that's similar to these 
numeric ranges.

The `coverage.py` program (used for measuring Python code coverage when testing) produces ranges of numbers similar 
to the format we're working with. The output from coverage.py sometimes includes ASCII arrows to show that one line 
jumped to another part of the program.

For the third bonus I want you to modify your function so that it accepts ranges with a single number followed by 
an `->` and a number or word and ignores the `->` and the thing that comes after it.

For example we include 20 here, but ignore `->` and `exit`:

    >>> list(parse_ranges('0, 4-8, 20->exit, 43-45'))
    [0, 4, 5, 6, 7, 8, 20, 43, 44, 45]
