# is_perfect_square

This week I want you to write a function that might seem simple at first, but there's a number of ways to solve it.

This week's function, `is_perfect_square`, accepts a number and returns `True` if it's a perfect square and `False` if it's not. A perfect square is any number which has an integer square root. So 25 is a perfect square but 24 is not, 9 is a perfect square but 8 is not, 100 is a perfect square but 1000 is not.

Here's an example:

    >>> is_perfect_square(64)
    True
    >>> is_perfect_square(65)
    False
    >>> is_perfect_square(100)
    True
    >>> is_perfect_square(1000)
    False

I also want you to make sure that this function raises a `TypeError` when an invalid type is given (integers and floats are fine but strings aren't) and I want you to make sure your function works with sensible alternative numeric types like `decimal.Decimal`.

There are a few bonuses this week. The second two are particularly tricky.

#### Bonus 1

The first bonus is to make sure your function returns `False` for negative numbers.

    >>> is_perfect_square(-1)
    False
    >>> is_perfect_square(-4)
    False

#### Bonus 2

The second bonus is to make sure your function works for really big numbers.

    >>> is_perfect_square(4624000000000000)
    True
    >>> is_perfect_square(4623999999999999)
    False

#### Bonus 3

The third bonus is to make your function accept an optional `complex` keyword-only argument which will allow your function to check whether the given number is a perfect square in the complex number system.

    >>> is_perfect_square(-4, complex=True)
    True
    >>> is_perfect_square(-5, complex=False)
    False
    >>> is_perfect_square(512j, complex=True)
    True

To be a complex perfect square, the complex square root of the number must have integers for both its real part and its imaginary part.

Note that you don't need to handle really big complex numbers.
