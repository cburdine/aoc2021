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

def magnitude(n):
    if n.v != None:
        return n.v
    return 3*magnitude(n.lc) + 2*magnitude(n.rc)

def main():
    lines = sys.stdin.readlines()
    
    tree = None
    for i, line in enumerate(lines):
        if tree == None:
            tree = make_tree(eval(line.strip()))
        else:
            subtree = make_tree(eval(line.strip()))
            n = Node(None,None)
            n.lc = tree
            n.rc = subtree
            n.lc.p = n.rc.p = n
            tree = n
        #print(f'tree[{i}]:')
        #print(tree)
        #print('reduced: ')
        reduce_tree(tree)
        #print(tree)

    print(tree)
    print('magnitude: ', magnitude(tree))
if __name__ == '__main__':
    main()
