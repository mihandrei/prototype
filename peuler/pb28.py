"""
Starting with the number 1 and moving to the right in a clockwise direction a 5 by 5 spiral is formed as follows:

21 22 23 24 25
20  7  8  9 10
19  6  1  2 11
18  5  4  3 12
17 16 15 14 13

It can be verified that the sum of the numbers on the diagonals is 101.

What is the sum of the numbers on the diagonals in a 1001 by 1001 spiral formed in the same way?
"""

"""
the edge of the k'th ring is d(k) = 2k+1 
ring k=1 is 23456789
then the perimeter(k) = 8k
the 1-9-15 diag is the area of the ring outerarea(k) = outerarea(k-1) + perimeter(k)
=> outerarea = 1 + 8*(1+2+...) = 1 + 4k(k+1)

the 1 7 21 diag is outerarea(k) - ( d(k) -1) => 4k**2+2k+1 

similar for other diags

The sum of all corners at a level k is S(k) = 4(4k**2+k+1)

The sum of all corners at all levels is 1 + sum ( S(k) ) k = 1..n

sumdiag(n) = 1 + (8 * n**2 + 15 * n + 13) * n * 2/3

"""

def sumdiag(n):
    return 1 + (8 * n**2 + 15 * n + 13) * n * 2/3


maxd = 1001
n = maxd/2
print sumdiag(n)