from collections import deque
import math

def read_tri(pth):
    ret = []
    with open(pth) as f:
        for l in f:
            ret.append([int(i) for i in l.split()])
    return ret
  

class Node(object):
    def __init__(self, idx, path, cost):
        self.path = path
        self.id = idx
        self.cost = cost

    def __repr__(self):
        return str(self.path[-1])    


def breadth_first(tr):
    fringe = deque()
    fringe.appendleft( Node( (0,0), [tr[0][0]], tr[0][0]) )

    def add_to_fringe(depth, b, parent):
        new_cost = parent.cost + tr[depth][b] 

        for n in fringe:
            if n.id == (depth, b):
                if n.cost < new_cost:
                    n.cost = new_cost
                    n.path = parent.path + [tr[depth][b]]
                return
        # not in fringe, append
        fringe.appendleft(Node((depth, b), parent.path + [tr[depth][b]], new_cost))

    fringe_ops = 0
    while fringe:
        fringe_ops+=1
        node = fringe.pop()
        depth, i = node.id
        if depth + 1 >= len(tr):
            print 'breadth_first ops %d' %fringe_ops
            return fringe
        add_to_fringe(depth + 1, i, node) #left
        add_to_fringe(depth + 1, i + 1, node)        


def min_path(tr):
    fringe = breadth_first(tr)
    
    best = fringe.pop()

    for n in fringe:
        if n.cost > best.cost:
            best = n
    return best
    

def pb18():
    best = min_path(read_tri('p018_triangle.txt'))
    print best.path
    print best.cost


def pb67():
    best = min_path(read_tri('p067_triangle.txt'))
    print best.path
    print best.cost

#pb67()

def p99():
    nrs = []
    with open('p099_base_exp.txt') as f:
        for l in f:
            nrs.append([int(a) for a in l.split(',')])
    
    nrs_ln = [e*math.log(b) for b, e in nrs]

    maxim = 0
    maxidx = -1

    for i, n in enumerate(nrs_ln):
        if n > maxim:
            maxim = n
            maxidx = i

    print maxidx, nrs[maxidx]


p99()
