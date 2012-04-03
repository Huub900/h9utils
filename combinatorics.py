# vim: set fileencoding=utf-8 :
from functools import reduce
from operator import mul


def fact(n):
    """
    Calculates factorial of n.
    >>> fact(0)
    1
    >>> fact(1)
    1
    >>> fact(5)
    120
    """

    if n < 0:
        raise ValueError
    elif n == 0 or n == 1:
        return 1
    else:
        return reduce(mul, range(2, n + 1))


def choices(n, k):
    """
    Binomial coefficient.
    >>> choices(7, 0)
    1
    >>> choices(7, 1)
    7
    >>> choices(7, 5)
    21
    """
    result = 1
    for i in range(1, k + 1):
        result = result * (n - i + 1) // i
    return result
