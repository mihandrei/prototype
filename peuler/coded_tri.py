import math
alphabet = 'abcdefghijklmnopqrstuvwxyz'

def word_s(w):    
    return sum(alphabet.index(a.lower()) + 1 for a in w)

def is_square(x):
    sq = math.ceil(x**0.5)
    return sq**2 == x

def is_triangle_number(t):
    # a triangular number is mod 3 0 or mod 9 1
    if t % 3 != 0 and t % 9 != 1:
        return False
    # solve for n and get 2n = sqrt(8t+1) - 1    
    return is_square(8*t + 1)


def process():
    with open('p042_words.txt') as f:
        w = [a[1:-1] for a in f.read().split(',')]
        w = [word_s(a) for a in w]
        
        i=0
        for a in w:
            if is_triangle_number(a):
                i+=1
        print len(w), i

process()
