# -*- coding: utf8 -*-
"""
Find the value of n ≤ 1,000,000 for which n/φ(n) is a maximum.
TODO: replace the totient function with one that has no rounding issues
TODO: replace all this brute forcing
"""

from sieve import factor, sieve

# def totient(n, cached_primes=None):
#     m = 1
#     for p, e in factor(n, cached_primes):
#         m *= (1 - 1.0/p)
#     return int(n * m)

def totient(n, cached_primes=None):
    t = 1
    for p, e in factor(n, cached_primes):
        t *= p**(e - 1) * (p - 1)
    return t

def p_69():
    max_n_phi = 0
    n_max = 0
    M = 10**6
    cached_primes = sieve(M + 1)

    for n in xrange(2, M):
        n_phi = float(n)/totient(n, cached_primes)
        if n_phi > max_n_phi:
            max_n_phi    = n_phi
            n_max = n

    print n_max, max_n_phi  


    # note : there is a pen and paper method of finding the result!!

def p_70():
    # brute
    candidates = []
    M = 10**7
    cached_primes = sieve(M + 1)

    for n in xrange(10**6, M):
        tot = totient(n, cached_primes)
        if sorted(str(tot)) == sorted(str(n)):
            candidates.append((n, tot))

    print len(candidates)

    n_min = 0
    ratio = M
    for n, tot in candidates:
        r = float(n)/tot
        if r < ratio:
            ratio = r
            n_min = n
    print n_min, ratio


# totient is wrong! shit!
# p_70()
# print totient(9708131) == 9701831, 9708131.0/9701831
# print factor(9708131)
