'''
The fraction 49/98 is a curious fraction, as an inexperienced mathematician in attempting to simplify 
it may incorrectly believe that 49/98 = 4/8, which is correct, is obtained by cancelling the 9s.

We shall consider fractions like, 30/50 = 3/5, to be trivial examples.

There are exactly four non-trivial examples of this type of fraction, less than one in value, 
and containing two digits in the numerator and denominator.

If the product of these four fractions is given in its lowest common terms, find the value of the denominator.
'''

def p33():
    print 'type ab/ca'

    for a in xrange(1, 10):
        for c in xrange(1,9):
            for b in xrange(1, c):
                if (10*a+b) * c == b * (10*c+a):
                    print '%d%d/%d%d' % (a,b,c,a)


    print 'type ab/ac'

    for a in xrange(1, 10):
        for c in xrange(1,9):
            for b in xrange(1, c):
                if (10*a+b) * c == b * (10*a+c):
                    print '%d%d/%d%d' % (a,b,a,c)


    print 'type ba/ca'

    for a in xrange(1, 10):
        for c in xrange(1,9):
            for b in xrange(1, c):
                if (10*b+a) * c == b * (10*c+a):
                    print '%d%d/%d%d' % (b,a,c,a)

    print 'type ba/ac'

    for a in xrange(1, 10):
        for c in xrange(1,9):
            for b in xrange(1, c):
                if (10*b+a) * c == b * (10*a+c):
                    print '%d%d/%d%d' % (b,a, a,c)

    from fractions import Fraction
    print Fraction('16/64')* Fraction('26/65')* Fraction('19/95')* Fraction('49/98')
    print 16.0/64*26/65*19/95*49/98


def factorial(n):
    r = 1
    for i in xrange(2, n+1):
        r*=i
    return r

def search_upperb():
    for n in xrange(1, 100):
        if 10**n - 1 > factorial(9) * n:
            return 10**(n-1) - 1

def digits_of_nr(n):
    result = []
    d = n

    while True:
        d, r = divmod(d, 10)    
        result.append(r)
        if d == 0:
            return result[::-1]


def digit_factorial_sum(n):
    return sum(factorial(d) for d in digits_of_nr(n))


def p34():
    max_number = search_upperb()
    for n in xrange(11, max_number):
        if digit_factorial_sum(n) == n:
            print n

def digits_to_nr(digits):
    nr = 0
    for i in xrange(len(digits)):
        nr += digits[len(digits)-1-i]*10**i
    return nr 


def list_rotations(nl):    
    rot = nl
    result = []

    for i in xrange(len(nl) - 1 ): # exclude nl from the rotation set
        rot = rot[1:] + [rot[0]]
        result.append(rot)
    return result


def number_rotations(n):
    return [digits_to_nr(rot) for rot in list_rotations(digits_of_nr(n))]



from sieve import sieve


def pb35():
    primes = set(sieve(10**6))

    circular_count = 0

    for p in primes:        
        circular = True

        for r in number_rotations(p):
            if r not in primes:
                circular = False
                break
        if circular:
            circular_count+=1

    print circular_count


def may_have_prime_rotations(p_digits):
    # rotations wil place the 2, etc at the end, no chance of primeness
    # but this optimization is weak as the roation search is cheap enough 
    if len(p_digits) > 1:        
        for i in [0, 2, 4, 5, 6, 8]:
            if i in p_digits:
                return False
    return True        


def pb35_slighly_optim():
    primes = set(sieve(10**6))

    circular_count = 0
    
    for p in primes:        
        p_digits = digits_of_nr(p)
        
        if not may_have_prime_rotations(p_digits):
            continue
        
        circular = True

        for r in list_rotations(p_digits):
            r = digits_to_nr(r)
            if r not in primes:
                circular = False
                break
        if circular:
            circular_count+=1

    print circular_count


pb35_slighly_optim()