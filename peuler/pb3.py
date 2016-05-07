# -*- coding: utf8 -*-
def pb_pali4():
    """
    A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

    Find the largest palindrome made from the product of two 3-digit numbers.
    """
    palins = {}    
    # brute force: generate all products, o(n**2)
    i=0
    for a in xrange(999, 100, -1):
        if a % 10 == 0: continue     # small prunning, palins are not multiple of 10 
        for b in xrange(a, 100, -1): # prunning: ab=ba generate only half the multiplication table
            i+=1
            s = str(a*b)
            if s == s[::-1]:                
                palins[a*b]=a,b

    # any info on the distrubution of palins to reduce the search space?
    # Order in a*b is not trivial-> partitioned by hyperbolae ab=ct -> a=ct/b
    # Can we aprox this order so that we can search first in the high product areas?
    print len(palins), i
    print max(palins.keys()), palins[max(palins.keys())]


def pb_5():
    """
    2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

    What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
    """

    # lcm(1..20) = lcm(lcm(1,2), 3..20) -> yuppy recursive def
    # lcm(1,2) = 1*2/gcd(1,2)   -> gcd euclid fast
    import fractions
    upto = 20
    
    g = 2
    for i in xrange(g + 1, upto + 1):    
        g = g * i / fractions.gcd(g, i)
    return g

# print pb_5()


def pb_6(k):
    """
    The sum of the squares of the first ten natural numbers is,

    1**2 + 2**2 + ... + 10**2 = 385
    The square of the sum of the first ten natural numbers is,

    (1 + 2 + ... + 10)**2 = 55**2 = 3025
    Hence the difference between the sum of the squares of the first ten natural numbers and 
    the square of the sum is 3025 − 385 = 2640.

    Find the difference between the sum of the squares of the first one hundred natural 
    numbers and the square of the sum.
    """
    square_of_sum = ( k*(k+1)/2 )**2
    sum_of_squares = k * (k+1) * (2*k+1) / 6
    print square_of_sum, sum_of_squares
    return square_of_sum - sum_of_squares

# print pb_6(100), 
  

def pb_9_brute(psum=1000):
    """
    A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

    a**2 + b**2 = c**2
    For example, 3**2 + 4**2 = 9 + 16 = 25 = 5**2.

    There exists exactly one Pythagorean triplet for which a + b + c = 1000.
    Find the product abc.
    """
    for c in xrange(1, psum):
        for b in xrange(1, c):
            a = psum - b - c
            if 0 < a < b and a**2 + b**2 == c**2:
                print a, b, c, a*b*c

def pb_9_on(psum=1000):
    """
    from a+b+c=psum and a,b,c pyth => b = psum * (psum/2-a) / (psum-a) 
    but we also have the converse b of that form along with a+b+c=psum => a,b,c pyth triple   
    """
    for a in xrange(1, psum):
        b = psum * (psum / 2.0 - a) / (psum - a)
        if b > a and b.is_integer():
            b = int(b)            
            c = psum - a - b
            print a, b, c, a*b*c
            

pb_9_on(2560000)
#pb_9_on(1000)
