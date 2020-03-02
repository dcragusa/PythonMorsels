import math
import cmath
import decimal
from numbers import Number

# def is_perfect_square(num):
#     if not isinstance(num, Number):
#         raise TypeError
#     sqrt = math.sqrt(num)
#     return math.isclose(sqrt, round(sqrt))

# def is_perfect_square(num):
#     if not isinstance(num, Number):
#         raise TypeError
#     if num < 0:
#         return False
#     sqrt = math.sqrt(num)
#     return math.isclose(sqrt, round(sqrt))

# def is_perfect_square(num):
#     if not isinstance(num, Number):
#         raise TypeError
#     if num < 0:
#         return False
#     if (numlength := len(str(num))) > 28:
#         decimal.getcontext().prec = numlength
#     sqrt = decimal.Decimal(num).sqrt()
#     return sqrt == round(sqrt)


def is_perfect_square(num, *, complex=False):
    if not isinstance(num, Number):
        raise TypeError
    if complex is True:
        sqrt = cmath.sqrt(num)
        return cmath.isclose(sqrt.real, round(sqrt.real)) and cmath.isclose(sqrt.imag, round(sqrt.imag))
    if num < 0:
        return False
    if (numlength := len(str(num))) > 28:
        decimal.getcontext().prec = numlength
    sqrt = decimal.Decimal(num).sqrt()
    return sqrt == round(sqrt)
