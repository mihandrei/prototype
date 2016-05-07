from sieve import sieve

def ciph_filter(x):
    ciph = [1, 3, 7, 9]# bad heuristics 23 should be ok!!!
    sef = [3, 7]    
    return x[0] in sef and x[-1] in sef and set(x) <= set(ciph)

def l_to_n(l):
    r = 0
    for i, n in enumerate(reversed(l)):
        r+= n * 10 **i
    return r

def is_trunky_prime(x):
    s = [int(a) for a in str(x)]
    if len(s) == 1 or not ciph_filter(s):
        return False

    for cut in xrange(1, len(s)):
        tl = s[:cut]
        tr = s[-cut:]
        tl = l_to_n(tl)
        tr = l_to_n(tr)

        if not tl in primes or not tr in primes:
            return False
    return True


def is_trunky_prime2(x):
    i = 1
    while True:
        d, m = divmod(x, 10**i)        
        if d == 0:
            return i > 1
        else:
            i+=1
        if not m in primes or d not in primes:
            return False

primes = sieve(10**7)
print len(primes)

t_pr = [p for p in primes if is_trunky_prime2(p)]
print t_pr

# t_pr = [p for p in primes if is_trunky_prime(p)]
# print t_pr