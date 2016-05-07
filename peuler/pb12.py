from sieve import factor, sieve
import math

def triangular_divisors(n):
    if n%2==0:
        af = factor(n/2)
        bf = factor(n+1)
    else:
        af = factor((n+1)/2)
        bf = factor(n)

    triangular_factors = af + bf
    
    ndivizors = 1
    for p, e in triangular_factors:
        ndivizors *= (e+1)
    return ndivizors


def pb12():
    """
    What is the value of the first triangle number to have over five hundred divisors?
    """
    for i in xrange(2, 10**9):
        td =  triangular_divisors(i)
        if (td >= 500):
            print i, td, i*(i+1)/2, factor(i*(i+1)/2)
            break

collatz_memo = {}

def next_collatz(n):   
    if n in collatz_memo:
        return collatz_memo[n] 
    if n % 2 == 0:
        r = n / 2
    else:
        r = 3 * n + 1
    collatz_memo[n] = r
    return r


def collatz_chain(n):
    seq = [n]
    while True:
        n = next_collatz(n)
        seq.append(n)
        if n == 1:
            return seq


def collatz_chain_len(n):
    seqlen = 0
    while True:
        n = next_collatz(n)
        seqlen +=1
        if n == 1:
            return seqlen

def pb14():
    """
    Considering the collatz sequence
    Which starting number, under one million, produces the longest chain?
    """
    maxlen = 0
    maxstart = 0

    for i in xrange(2, 10**6):
        l = collatz_chain_len(i)
        if l > maxlen:
            maxlen = l
            maxstart = i
    print maxstart, l

# pb14()

def factorial(n):
    f = 1
    for i in xrange(1, n+1):
        f*=i
    return f

def pb20():
    "Find the sum of the digits in the number 100!"
    # as in the 2**1000 problem there is no reasonable math attack
    # in the 2*1000 problem : length of number is 1000*log(2,10), assuming uniform digit distribution
    # one gets sum(2**k) = 5 * k * log(2,10) ~= 1.505 * k
    # Experiments of ploting sum(2**k) shows indeed a linear trend with noise, but the slope is ~ 1.34
    # So the uniformity is not exact
    
    #print factorial(100)
    print sum(int(i) for i in str(factorial(100)))
# pb20()
# y=[]
# for n in xrange(2, 300):
#     y.append(sum(int(i) for i in str(factorial(n))))
# from matplotlib import pyplot
# pyplot.plot(y)
# pyplot.show()



