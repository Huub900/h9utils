# vim: set fileencoding=utf-8 :
"""Number theory utilities."""


def gcd(a, b):
    """Greatest common divisor -- Euclidean algorithm."""
    while b != 0:
        a, b = b, a % b
    return a


def lcm(a, b):
    """Least common multiple."""
    return a * b // gcd(a, b)
