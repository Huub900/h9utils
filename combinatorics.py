# vim: set fileencoding=utf-8 :
"""Combinatorics utilities"""

from functools import reduce
from operator import mul


def fact(n):
    """Factorial of n.

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
    """Binomial coefficient.

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


def stirling2(n, k):
    """Stirling numbers of second kind.

    >>> stirling2(3, 4)
    0
    >>> stirling2(8, 5)
    1050
    """
    result = 0
    for i in range(k + 1):
        result += (-1) ** (k - i) * choices(k, i) * i ** n
    result //= fact(k)
    return result
