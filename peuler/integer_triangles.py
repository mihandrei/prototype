"""
For which p < 1000 is the number of solutions maximized

There is a nice theorem generating all fundamental pythagoreean triples
There exist m, n such as m > n m,n coprime m-n odd

a = m**2-n**2
b = 2mn
c = m**2 + n**2

(this representation is unique if m,n coprime and m-n odd)

The non-funamental ones are a = ka b = kb c = kc

perimeter p is p = 2 k m (m + n)

=> odd perimeters no solutions
some bounds:
  note that n >=1 => m>=2. This and p formula =>
  k <= p/12
  m <= sqrt(p/2)
  n < m
  oddly a k m n loop to check solutions is o(N)**2 as the m, n loops are up to sqrt
  This makes a global search upto p a cubic algorithm
  Of course the first 2 iter variables will skip ks and m's that do not divide p
"""
import math

def kmn_to_abc(k, m, n):
    a = m**2 - n**2
    b = 2*m*n
    c = m**2 + n**2
    return a*k, b*k, c*k


def search(p):
    sol = []

    if p % 2 != 0:
        return []
        
    i = 0
    
    for k in xrange(1, p/12 + 1):
        if p % k != 0: # divizibility prunning
            continue
        # sweet bounds
        max_m = int(math.ceil((p/2/k)**0.5))
        min_m = int(math.floor((p/k/4.0)**0.5))

        for m in xrange(max(min_m, 2), max_m + 1):
            if p % m != 0:
                continue
            for n in xrange(1, m):
                if (m-n)%2==0:
                    continue
                i+=1
                if p == 2*k*m*(m+n):
                    sol.append((k, m, n))

    # print '%d iters and %d solutions' % (i, len(sol))
    return sol


def find_abundant_perimeter(upto):
    sol = {}
    for p in xrange(4, upto, 2):
        s = search(p)
        if s:
            sol[p] = len(s)
    return sol

# s = search(120)
# sabc = [kmn_to_abc(k, m, n) for k, m, n in s] 
# print s
# print sabc
m = 0
pm = 0
for k, v in find_abundant_perimeter(1001).iteritems():
    if v > m:
        m = v
        pm = k
print pm , m