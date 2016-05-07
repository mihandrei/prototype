"""
prime number stuff
"""

from fractions import gcd
from random import randint

# some wheel optimization for 3 would be nice
# this wheels only 2
# also a numpy bit array might be faster
def sieve(upto):
    sv = [True for _ in xrange(3,upto,2)]
    
    for a in xrange(3, 1+int(upto**0.5), 2):
        i = a/2-1
    
        if sv[i]: # a prime
            for b in xrange(a**2, upto, 2*a):
                j = b/2-1
                sv[j] = False
    
    return [2]+[i*2+3 for i,p in enumerate(sv) if sv[i]]    


#print sum(sieve(2*10**6))

def factor(n, cached_sieve=None):
    ''' 
    trial division by primes
    cached_sieve optionally give a prime list if repeated factoring is used 
    '''
    factors = []

    max_prime = int(n**0.5)+1

    if cached_sieve is not None:
        primes = cached_sieve
    else:
        primes = sieve(max_prime+1)  # second +1 because sieve(upto) upto is open interval

    for p in primes:
        if p > max_prime:
            break
        power = 0
        while n%p == 0:
            power +=1
            n = n/p        
        if power:
            factors.append((p, power))
    if n > 1: #escaped sieving=> n itself prime
        factors.append((n,1))
    return factors
    

def modexp(a, e, m):
    "a**e mod m"
    a = a % m
    
    if e == 1:
        return a 

    r = modexp(a, e/2, m) ** 2    
    
    if e % 2 == 1:
        r *= a
    return r % m


def is_fermat_pseudo_prime(n, witnesses=[2, 3, 5, 7]):        
    for w in witnesses:
        if w > n:
            return True
        if gcd(w, n) == 1:
            if modexp(w, n - 1, n) != 1:
                return False
    return True
        
    # a = []        
    # for i in xrange(3, 1500, 2):
    #     if is_fermat_pseudo_prime(i):
    #         a.append(i)

    # print list(sorted(set(a) - set(sieve(1501))))