"""
Let d(n) be defined as the sum of proper divisors of n (numbers less than n which divide evenly into n).
If d(a) = b and d(b) = a, where a <> b, then a and b are an amicable pair and each of a and b are called amicable numbers.

For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; therefore d(220) = 284.
 The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.

Evaluate the sum of all the amicable numbers under 10000.
"""
from sieve import factor

                

def divisor_iter(n):    
    factorization = factor(n)

    # factorization of the current divisor
    divisor_fact = [(p, 0) for p, e in factorization]

    def _next_divisor_fact():
        """ count up from 2**0 * 3*0 * ... to the factorization"""
        for i in xrange(len(factorization)):
            dp, de = divisor_fact[i]
            if de < factorization[i][1]:                
                divisor_fact[i] = (dp, de + 1)
                return divisor_fact
            else: #overflow
                divisor_fact[i] = (dp, 0)
                if i == len(factorization) - 1:
                    return None

    def _compute_divisor():
        mul = 1
        for p, e in divisor_fact:
            mul *= p**e
        return mul


    while True:
        yield _compute_divisor()
        if not _next_divisor_fact():
            return



def proper_divisor_sum(n):
    return sum(divisor_iter(n)) - n


amicable = {}

for n in xrange(2, 10000):
    if n in amicable:
        continue
    s = proper_divisor_sum(n)
    if s!= n and proper_divisor_sum(s) == n:
        amicable[s] = n
        amicable[n] = s

print sorted(amicable)
print sum(amicable)