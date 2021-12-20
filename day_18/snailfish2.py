#!/bin/env python3

import sys

class Node:
    def __init__(self, v, p=None):
        self.p = p
        self.v = v
        self.lc = None
        self.rc = None
    
    def left_neighbor(self):
        ptr = self
        while ptr.p and ptr.p.lc == ptr:
            ptr = ptr.p
        if not ptr.p:
            return None
        if ptr.p.lc == ptr:
            return None
        ptr = ptr.p.lc
        while ptr.rc:
            ptr = ptr.rc
        return ptr

    def right_neighbor(self):
        ptr = self
        while ptr.p and ptr.p.rc == ptr:
            ptr = ptr.p
        if not ptr.p:
            return None
        if ptr.p.rc == ptr:
            return None
        ptr = ptr.p.rc
        while ptr.lc:
            ptr = ptr.lc
        return ptr

    def depth(self):
        d = 0
        ptr = self
        while ptr.p:
            ptr = ptr.p
            d += 1
        return d
    
    def __str__(self):
        if self.v == None:
            assert(self.lc != None)
            assert(self.rc != None)
            return '['+str(self.lc)+','+str(self.rc)+']'
        return str(self.v)

def make_tree(arr):
    if isinstance(arr,int):
        return Node(arr,None)
     
    n = Node(None,None)
    n.lc = make_tree(arr[0])
    n.rc = make_tree(arr[1])
    n.lc.p = n.rc.p = n
    return n 

def explode(n):
    if n.v != None:
        return False
    elif n.lc and n.lc.v != None and \
         n.rc and n.rc.v != None and \
         n.depth() >= 4:
        ln = n.lc.left_neighbor()
        rn = n.rc.right_neighbor()
        #print([n.lc.v, n.rc.v])
        if ln != None:
            assert(ln.v != None)
            ln.v += n.lc.v
        if rn != None:
            assert(rn.v != None)
            rn.v += n.rc.v
        n.lc = n.rc = None
        n.v = 0
        return True

    return explode(n.lc) or explode(n.rc)

def split(n):
    if n.v != None:
        if n.v < 10:
            return False
        lval = n.v//2
        rval = n.v-(n.v//2)
        n.lc = Node(lval,n)
        n.rc = Node(rval,n)
        n.v = None
        return True
    
    return split(n.lc) or split(n.rc)

def reduce_tree(n):
    while explode(n) or split(n):
        continue

    return n

def magnitude(n):
    if n.v != None:
        return n.v
    return 3*magnitude(n.lc) + 2*magnitude(n.rc)

def add_tree(n1,n2):
    n = Node(None,None)
    n.lc = n1
    n.rc = n2
    n.lc.p = n.rc.p = n
    return reduce_tree(n)

def main():
    lines = sys.stdin.readlines()

    lists = [
        eval(line.strip())
        for line in lines
    ]

    mags = {}
    for i, l1 in enumerate(lists):
        for j, l2 in enumerate(lists):
            if i != j:
                n1 = make_tree(l1)
                n2 = make_tree(l2)
                mags[(i,j)] = magnitude(add_tree(n1,n2))
        print(f'{i}/{len(lists)}')

    print('max magnitude: ', max(mags.values()))
    

if __name__ == '__main__':
    main()
