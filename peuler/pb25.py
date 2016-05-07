from math import log

def fibonacci(n):
    """
    simple O(n) implementation
    """
    p = 1
    f = 1

    for i in xrange(3, n+1):
        fn = f + p
        p = f
        f = fn

    return f


phi = (1 + 5**0.5) / 2.0

def fibonacci_float_aprox(n):
    'this is aproximative due to float precision'    
    return int(phi ** n / 5**0.5)


"""
What is the index of the first term in the Fibonacci sequence to contain 1000 digits
999 zeros and a leading one is 1000 digits
phi**n/5**0.5 > 10**999 =>
n > log(5**0.5 * 10**999, phi)
n > 0.5*log(5, phi) + 999*log(10, phi)
"""

aprox_n = 0.5 * log(5, phi) + 999 * log(10, phi)
print aprox_n
aprox_n = int(aprox_n)
# acum tatonam in jurul aproximarii pana cand gasim trecerea 999->1000
print len(str(fibonacci(aprox_n+1)))
print aprox_n+1