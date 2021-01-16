# comparator

This week I'd like you to create a class which allows the `==` operator to work as an "almost equal" comparison.

    >>> target_number = Comparator(0.12)
    >>> n = 0.1 + 0.02
    >>> n == 0.12
    False
    >>> n
    0.12000000000000001
    >>> n == target_number
    True

Your `Comparator` object should have a default delta value of 0.0000001 (meaning numbers should be no further 
than that from your target number). This delta value should be customizable.

    >>> close_to_five = Comparator(5, delta=0.1)
    >>> close_to_five == 5.05
    True
    >>> close_to_five == 4.98
    True
    >>> close_to_five == 5.2
    False

The greatest delta should be used when comparing two `Comparator` objects.

Your `Comparator` object should also have a nice string representation.

    >>> close_to_five
    Comparator(5, delta=0.1)
    >>> target_number
    Comparator(0.12, delta=1e-07)

#### Bonus 1

For the first bonus I'd like you to allow `Comparator` objects to be added and subtracted with other numbers:

    >>> almost_100 = Comparator(100, delta=1)
    >>> almost_50 = almost_100 - 50
    >>> almost_110 = 10 + almost_100
    >>> almost_50
    Comparator(50, delta=1)
    >>> 109 == almost_110
    True
    >>> 108 == almost_110
    False

#### Bonus 2

For the second bonus I'd like you to allow `Comparator` objects to be added and subtracted with other `Comparator` 
objects. The largest delta should be maintained when adding/subtracting:

    >>> nearly_five = Comparator(5, delta=0.1)
    >>> almost_100 = Comparator(100, delta=1)
    >>> almost_105 = almost_100 + nearly_five
    >>> almost_105
    Comparator(105, delta=1)

#### Bonus 3

For the third bonus, I'd like you to create a `Comparator.default_delta` context manager that allows the default 
`Comparator` delta to change within a context manager block:

    >>> import math
    >>> with Comparator.default_delta(0.005):
    ...     pi = Comparator(math.pi)
    ...     print(3.142, 3.142 == pi)
    ...     print(3.18, 3.18 == pi)
    ...
    3.142 True
    3.18 False

The default delta should only be changed inside the `Comparator` block.
