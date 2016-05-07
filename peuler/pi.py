def geometric_pi(k):
    '''
    based on simple geometric bisecting of angle
    l2n**2 = 2 - (2 - sqrt(4-ln**2))
    l6=1
    pn=n*ln
    ln -> 0 as n-> inf
    this is likely a bad numerical algo
    After some reading I identified this recurrence as close to the Viete formulas

    An interesting domain of pi calculation opens:
    * quadrature of an integral from a circle
    * atan nice power series caused by it's rational derivative
    * most interesting the arithmetic geometric mean
    '''
    l = 1
    for i in xrange(k):
        n = 3 * 2**i
        print l, n, n*l
        l = (2 - (4 - l**2)**0.5)**0.5
    n = 3 * 2**k
    pi = n*l
    print 'pi aprox with n %d is %f' % ( n, pi)

geometric_pi(8)

def agm(a, b, delta=1e-8):
    while abs(a-b) > delta:
        a, b = (a + b)*0.5, (a*b)**0.5
        print a, b
    return a

#agm(24, 6)
