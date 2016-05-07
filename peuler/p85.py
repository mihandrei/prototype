'''
counting rectangles in a grid of m by n

Although there exists no rectangular grid that contains exactly two million rectangles, 
find the area of the grid with the nearest solution.

Let the rectangle have the horizontal length a, and the other b

The a segment may be translated to the right (m-a) times
The b one n-b times
The number of positions is translations + 1 the original position with a point in 0,0
So pos(a) = m-a+1 pos(b) = n-a+1
For each positioning of a we can coose any position of b
So pos(rect_ab) = (m-a+1)(n-b+1)
All rectangles positions we get by iterating all a's and b's
pos(rects) = sum_a_1_m sum_b_1_n (m-a+1)(n-b+1)
           = m(m+1)n(n+1)/4

So the problem becomes finding a good aprox to this equation:

m(m+1)n(n+1)/4 ~= 2*10**6 = C

I see no analytical solution
Try to find some bounds for a search:

m(m+1)n(n+1)/4 ~= C let delta be the error term
m(m+1)n(n+1)/4 = C +- delta
As m=n=1 is a solution delta < C
so 
m(m+1)n(n+1)/4 < C +- C < 2*C

if m==1 the min then n(n+1) < 4C => n**2 + n < 4C  n**2 < 4C => n < 2 C**0.5
idem for m

So we have an upper bound for m and n

We can obtain a much better bound on delta by considering squares m==n whose scores are < C
C ~= m**2 (m+1)**2 / 4 < (m+1) ** 4 / 4
So ml = int( (4C)**1/4 - 1 ) is a rect with score under C
Thus delta < C - numrect(ml, ml)
OK now bounds m(m+1)n(n+1)/4 = C +- delta
m==1 m < sqrt(c+delta)

There is a lower bound as well m=2 m =3 has no chance
This is harder to pin as it requires a better estimate of delta

Without loss of generality we can have n <= m, halving the search space
We will minimize delta 
'''

def rectangles_in_grid(m, n):
    return m*(m+1)*n*(n+1)/4


def search(nrects=2*10**6):
    #upper_bound = int(2 * nrects**0.5)
    maximal_square_side = int((4 * nrects)**0.25) - 1 # biggest square with score under nrects    
    delta_upper_bound = nrects - rectangles_in_grid(maximal_square_side, maximal_square_side)
    upper_bound = int( (2*(nrects + delta_upper_bound))**0.5 )
    print upper_bound
    #todo better bounds, or incremental search on delta=0..delta_upper_bound
    mindelta = nrects
    sol = 1, 1

    for m in xrange(1, upper_bound):
        for n in xrange(1, m + 1):
            rects = rectangles_in_grid(m, n)
            delta = abs(nrects - rects)
            
            if delta < mindelta:
                mindelta = delta
                sol = m, n
            
    return sol, mindelta


sol, delta = search()
print sol, delta, sol[0]*sol[1], rectangles_in_grid(sol[0], sol[1])