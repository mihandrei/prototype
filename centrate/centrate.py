from itertools import permutations
from collections import defaultdict

INITIAL_SET = list(permutations('0123456789', 4))
ALL_ANSWERS = [(0, 0),
               (1, 0), (0, 1), 
               (2, 0), (1, 1), (0, 2), 
               (3, 0), (2, 1), (1, 2), (0, 3), 
               (4, 0), (2, 2), (1, 3), (0, 4)]

def evaluate(nr, question):
    centr, necentr = 0, 0
    for i, a in enumerate(question):
        if a in nr:
            j = nr.index(a)
            if j==i:
                centr += 1
            else:
                necentr +=1
    return centr, necentr

    
def restrict_solutions(solutions, question, a_c, a_nc):
    def number_fits_question(n):
        return evaluate(n, question) == (a_c, a_nc)

    return [s for s in solutions if number_fits_question(s)]


def question_distribution(solutions, question):
    """
    A set of solutions is given.
    The given question will have possible different answers for each solution in the set.
    Returns the distribution answer->subset of solutions giving this answer 
    """ 
    dist = defaultdict(int)
    for s in solutions:
        ev = evaluate(s, question)
        dist[ev]+=1
    return dist


def min_distribution(solutions):
    new_q = []
    min_score = 1000
    # a dumb but reasonable way to reduce the search space is to random sample some of the possible questions
    for q in INITIAL_SET:
        k = question_distribution(solutions, q)
        score = max(k.values())
        if score < min_score:
            min_score = score
            new_q = q
    # print 'at score %d found %s' %(min_score, new_q)
    return new_q


def answer(new_q):
    a = raw_input('answer %s :' % ''.join(new_q))
    a.strip().upper()
    c, nc = a.count('x'), a.count('0')+a.count('o')
    return c, nc


def score(solutions):
    if len(solutions) == 1:
        print 'your number is %s' % ''.join(solutions[0])
        return True
    elif len(solutions) == 0:
        print 'no solutions, you lied'
        return True
    elif len(solutions) < 10:
        print 'possible numbers %s' % [''.join(s) for s in solutions]        
    else:
        print 'possible numbers %d ' % len(solutions)
    return False

#check this table
PRECOM_1234 = {
    (0, 1): ('0', '1', '5', '6'), (1, 2): ('0', '2', '3', '5'), (0, 0): ('0', '5', '6', '7'), 
    (3, 0): ('0', '2', '3', '5'), (0, 4): ('0', '3', '4', '2'), (2, 1): ('0', '1', '3', '5'), 
    (0, 2): ('0', '3', '4', '2'), (2, 0): ('0', '1', '3', '5'), (1, 3): ('0', '1', '2', '3'), 
    (2, 2): ('0', '1', '2', '3'), (1, 0): ('0', '2', '3', '5'), (0, 3): ('0', '1', '2', '5'), 
    (1, 1): ('0', '2', '3', '5'), (4, 0): ('0', '1', '2', '3')}


def play():
    solutions = INITIAL_SET
    
    new_q = tuple('1234')
    c, nc = answer(new_q)
    solutions = restrict_solutions(solutions, new_q, c, nc)
    if score(solutions):
        return
    
    # optimization: next question after 1234 have been precomputed
    new_q = PRECOM_1234[(c, nc)]
    c, nc = answer(new_q)
    solutions = restrict_solutions(solutions, new_q, c, nc)        
    if score(solutions):
        return

    while True:
        new_q = min_distribution(solutions)        
        c, nc = answer(new_q)
        solutions = restrict_solutions(solutions, new_q, c, nc)        
        if score(solutions):
            return


def eval_ui():
    nr = raw_input('secret nr: ')
    nr = tuple(nr.strip())
    while True:
        q = raw_input('question : ')
        q = tuple(q.strip())
        c, nc = evaluate(nr, q)
        print 'x'*c + '0'*nc


import sys
if __name__ == '__main__':
    if len(sys.argv) > 1 and sys.argv[1] == 'e':
        print 'Answering questions'
        print
        eval_ui()
    print 'Trying to guess your number'
    print 
    play()
    