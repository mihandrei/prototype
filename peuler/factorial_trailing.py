def prime_factor_expo_of_factorial(n, p):
    """
    Prime factorization of factorials
    Legendre's theorem
    return the expoent of the prime p in the factorization of n!
    """
    niu = 0
    k = 1
    
    while True:        
        t = n / p**k
        niu += t
        k += 1
        if t == 0:            
            return niu
            


def trailing_zeros_in_factorial(n):
    '''
    we only need to consider the powers of 5. It is easy to show that for each power of 5 
    we have a correponding power of 2 thus a 10 is formed
    '''
    return prime_factor_expo_of_factorial(n, 5)


# print 'trail is %d' %trailing_zeros_in_factorial(10**12)

from sieve import modexp

def partial_factor(n, p):
    e = 0
    while n%p==0:
        e+=1
        n=n/p
    return e, n


def compute_period_product(period):
    prod = 1
    niu = prime_factor_expo_of_factorial(period, 5)
     
    for x in xrange(1, period + 1):       
        _, five_rst = partial_factor(x, 5)
        
        x = five_rst
        if niu > 0:
            two_e, two_rst = partial_factor(x, 2)
            if two_e > 0:
                if niu >= two_e:
                    niu -= two_e                    
                    x = two_rst
                else:
                    two_e = two_e - niu
                    niu = 0                    
                    x = two_rst * modexp(2, two_e, period)

        prod = (prod * x) % period        
        # print x, prod 
        
    return prod

def factorial(n):
    f = 1
    for i in xrange(2, n+1):
        f*=i
    return f

def test1():
    per = 10**5
    core = compute_period_product(per)
    print 'aa',  core
    print 'ref', (factorial(per)/10**prime_factor_expo_of_factorial(per, 5))%per

    print 'result', modexp(core, 10**7, per)

def test2():
    print prime_factor_expo_of_factorial(10**5, 5)

    print partial_factor(5*3, 5)

    # print factor(3, [2])#2**2*3**2*5**2*7*9, [2, 5])

def test3():
    a = []
    b = []
    for i in xrange(1, 40):
        a.append(i%10)
        e, r=partial_factor(i, 5)
        b.append('5^%d*%d' % (e,r) if e else '%d' % r)
    print a
    print b
test3()