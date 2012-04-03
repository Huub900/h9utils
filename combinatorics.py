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
