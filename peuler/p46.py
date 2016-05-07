"""
It was proposed by Christian Goldbach that every odd composite number can be written 
as the sum of a prime and twice a square.

It turns out that the conjecture was false.
What is the smallest odd composite that cannot be written as the sum of a prime and twice a square?

a = p + 2 * s**2, p prime , a odd composite

Some bounds

p <= a - 2
s <= sqrt(a/2 - 1)

"""
from sieve import sieve
import math

MAXA = 10000
primes = sieve(MAXA + 1)

def check(a):
    maxs = int(math.ceil((a/2.0 - 1)**0.5))
    for s in xrange(1, maxs):
        p = a - 2 * s**2
        if p in primes:
            return True
    return False

for a in xrange(3, MAXA, 2):
    if a in primes:
        continue
    if not check(a):
        print a

