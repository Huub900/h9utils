# vim: set fileencoding=utf-8 :
"""Combinatorics utilities"""

from functools import reduce
from operator import mul


def fact(n):
    """Factorial of n."""
    if n < 0:
        raise ValueError
    elif n == 0 or n == 1:
        return 1
    else:
        return reduce(mul, range(2, n + 1))


def choices(n, k):
    """Binomial coefficient."""
    result = 1
    for i in range(1, k + 1):
        result = result * (n - i + 1) // i
    return result


def stirling2(n, k):
    """Stirling numbers of second kind."""
    result = 0
    for i in range(k + 1):
        result += (-1) ** (k - i) * choices(k, i) * i ** n
    result //= fact(k)
    return result


def n_parts(n, k):
    """Number partitions"""
    if n == k:
        return 1
    elif n < k or k < 1:
        return 0
    else:
        return n_parts(n - 1, k - 1) + n_parts(n - k, k)
