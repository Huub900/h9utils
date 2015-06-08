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


def fib(n):
    """Fibonacci number."""
    if n == 0: return 0
    if n == 1: return 1
    a, b = 0, 1
    for i in range(2, n + 1):
        a, b = b, a+b
    return b
