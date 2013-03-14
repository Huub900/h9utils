from combinatorics import choices

def binom(p, n, k):
    return choices(n, k) * p ** k * (1 - p) ** (n - k)