'''
add theory:

lema: a is uneven
lema: height and semibase are integers -> hlaf the triangle is pythagoreean triple
'''
import math

def quadratic_residues(modulo):
    return set(i**2 % modulo for i in xrange(modulo/2+1))

rezidues_32 = quadratic_residues(32)

def is_square(x):
    if x%32 not in rezidues_32:        
        return False
    sq = math.ceil(x**0.5)
    return sq**2 == x


def brute_force_explore(aupto):
    for a in xrange(3, aupto, 2):
        for delta in [-1, 1]:
            h2 = (3*a + delta) * (a - delta) / 4
            if is_square(h2):
                print 'a=%d, b=%d, h=%d, A=%d, p=%d, delta=%d' % (a, a + delta, h2**0.5, (a+delta)/2 * h2**0.5, 3*a+delta, delta)


# brute_force_explore()

def explore_c1(mupto):
    for m in xrange(2, mupto):
        # only delta 1 considered
        # note delta -1 => x = (m**2+1)/3 dar m**2+1 nu se imparte veci la 3
        if m%3 == 0:
            # for 0 residue m**2-1 = -1 si nu ne imprtim la 3, altfel da
            continue
        x = (m**2 - 1)/3
        
        if is_square(x):
            n = int(x**0.5)
            a = m**2 + n**2
            b = 2 * (m**2 - n**2)
            p = 4*m**2
            if p > 10**9:
                return
            print 'a=%d, b=%d, p=%d @ m=%d, n=%d' % (a, b, p, m, n)

def explore_c2(mupto):
    for m in xrange(1, mupto):
        for delta in [-1,1]:
            x = 3*m**2 - delta
            if is_square(x):
                n = int(2*m + x**0.5)
                a = m**2 + n**2
                b = 2 * 2 * m * n
                p = 3*a + delta
                if p > 10**9:
                    return
                print 'a=%d, b=%d, p=%d @ m=%d, n=%d' % (a, b, p, m, n)

# brute_force_explore(10**6)
print '='*12
explore_c1(10**5)
print '='*12
explore_c2(10**5)


rez = 518408346

'''
Note: This approach searches fundamental pitagorean triples of a certain kind using the 
representation theorem of pythg triples

There is however a way to reduce this to a pell equation, which has a standard enumerable set of solutions.
'''
