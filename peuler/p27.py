from sieve import sieve, is_fermat_pseudo_prime

primes = sieve(1000000)

print 'sieve done'

def prime_run(a, b):
    '''
    n**2+an+b
    n=b => n**+an+n not prime
    range of |n| is 0..b-1
    '''
    r = []
    for n in xrange(b):    
        y = n**2 + a*n + b
        if y > 0 and is_fermat_pseudo_prime(y):
            if y in primes:
                r.append(y)
        else:
            break
    return r
    


def prime_generating_quadratic(max_coef):
    maxlen = 0
    maxpoli = 0, 0
    maxprime_run = []
    for a in xrange(-max_coef+1, max_coef):
        for b in xrange(-max_coef+1, max_coef):
            pr = prime_run(a, b)
            if len(pr) > maxlen:
                maxlen = len(pr)
                maxpoli = a, b 
                maxprime_run = pr
    print 'n**2 + (%d)n + (%d)' % (maxpoli)
    print len(maxprime_run)

# print len(prime_run(-79, 1601))
prime_generating_quadratic(1000)
print 61*971
