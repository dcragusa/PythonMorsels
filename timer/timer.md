# Timer

This week I'd like you to write a context manager called `Timer` which will record how long a block of code takes to execute.

    >>> from time import sleep
    >>> with Timer() as timer:
    ...     sleep(1.5)
    ...
    >>> timer.elapsed
    1.504882783210324

#### Bonus 1

For the first bonus I'd like you to record the elapsed times of each usage of the context manager in a `runs` attribute.

    >>> timer = Timer()
    >>> with timer:
    ...     x = sum(range(2**24))
    ...
    >>> timer.elapsed
    0.2696345190051943
    >>> with timer:
    ...     x = sum(range(2**25))
    ...
    >>> timer.elapsed
    0.5121023440151475
    >>> timer.runs
    [0.2696345190051943, 0.5121023440151475]

#### Bonus 2

For the second bonus I'd like you to allow `Timer` to be used as a decorator too:

    >>> @Timer
    ... def sum_of_squares(numbers):
    ...     return sum(n**2 for n in numbers)
    ...
    >>> sum_of_squares(range(2**20))
    384306618446643200
    >>> sum_of_squares(range(2**21))
    3074455146595352576
    >>> sum_of_squares.runs
    [0.35114182299003005, 0.6639977040467784]

#### Bonus 3

For the third bonus I'd like you to maintain `min`, `max`, `mean`, and `median` properties that keep track of these values for all runs in a given timer:

    >>> sum_of_squares(range(2**19))
    48038258586419200
    >>> sum_of_squares(range(2**22))
    24595649968853745664
    >>> sum_of_squares.runs
    [0.35114182299003005, 0.6639977040467784, 0.19335223210509866, 1.3423286559991539]
    >>> sum_of_squares.mean
    0.6377051037852652
    >>> sum_of_squares.median
    0.5075697635184042
    >>> sum_of_squares.min
    0.19335223210509866
    >>> sum_of_squares.max
    1.3423286559991539
