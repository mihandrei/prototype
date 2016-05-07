import math
from fractions import Fraction
# could do without the fraction class but then we have to esentially implement them 
# addition and reciprocals are required as well as gcd reduction

def to_fraction(cont_fr, fract_type=float):
    x = fract_type(cont_fr[-1])

    for i in xrange(-2, -len(cont_fr)-1, -1):        
        x = cont_fr[i] + 1/x 
    
    return x


def convergents(cont_fr, fract_type=float):
    res = []
    for cutoff in xrange(2, len(cont_fr)+1):
        res.append(to_fraction(cont_fr[:cutoff], fract_type))
    return res

#print to_fraction([1,2,2,2])
# print convergents([1] + [2]*4)
# print convergents([1] + [2]*4, Fraction)

def pb57():
    '''
    In the first one-thousand expansions of sqrt(2), how many fractions contain a numerator 
    with more digits than denominator?
    sqrt(2) = [1;2,2,2,2,...]
    '''
    count = 0
    for c in convergents([1] + [2] * 1000, Fraction):
        if math.floor(math.log10(c.numerator)) > math.floor(math.log10(c.denominator)):
            count+=1
        # if len(str(c.numerator)) > len(str(c.denominator)):
            # count+=1
    print count

pb57()