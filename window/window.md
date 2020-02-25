# window

This week I'd like you to write a function that returns "windows" of items from a given list. Your function should take an iterable and a number n and return a list of tuples, each containing "windows" of n consecutive items. That is, each tuple should contain the current item and the n-1 items after it.

Here are some examples:

    >>> numbers = [1, 2, 3, 4, 5, 6]
    >>> window(numbers, 2)
    [(1, 2), (2, 3), (3, 4), (4, 5), (5, 6)]
    >>> window(numbers, 3)
    [(1, 2, 3), (2, 3, 4), (3, 4, 5), (4, 5, 6)]
    >>> squares = (n**2 for n in numbers)
    >>> window(squares, 4)
    [(1, 4, 9, 16), (4, 9, 16, 25), (9, 16, 25, 36)]

Your window function should return an empty list if the given n is 0. It should also be to accept strings, tuples, and any other iterables.

I recommend solving the base problem before any of the bonuses this week.

#### Bonus 1

As a bonus, make sure your function returns an iterator instead of a list.

    >>> numbers = [1, 2, 3, 4, 5, 6]
    >>> next(window(numbers, 3))
    (1, 2, 3)

#### Bonus 2

For a more challenging bonus, make your function works with values of n that are longer than the given iterable by filling the tuple with `None` values.

    >>> list(window([1, 2, 3], 6))
    [(1, 2, 3, None, None, None)]

#### Bonus 3

If you manage to solve all of that in the time you've scheduled for this exercise, there's one more bonus. Allow a `fillvalue` keyword argument to be specified to be used instead of `None` when the window length is longer than the iterable:

    >>> list(window([1, 2, 3], 5, fillvalue=0))
    [(1, 2, 3, 0, 0)]

Make sure that `fillvalue` only works as a named argument though. Specifying `fillvalue` as a positional argument wouldn't be as clear and shouldn't be allowed.
