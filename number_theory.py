# vim: set fileencoding=utf-8 :


def gcd(a, b):
    """
    Greatest common divisor -- Euclidean algorithm.
    >>> gcd(0, 5)
    5
    >>> gcd(1071, 1029)
    21
    """
    while b != 0:
        a, b = b, a % b
    return a


def lcm(a, b):
    """
    Least common multiple.
    >>> lcm(1071, 1029)
    52479
    """
    return a * b // gcd(a, b)
