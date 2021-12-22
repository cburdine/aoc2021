#!/bin/env python3

import sys
from collections import defaultdict
from itertools import product

def main():

    lines = sys.stdin.readlines()
    
    instructions = []
    ranges = []
    for line in lines:
        instr, coords = line.strip().split(' ')
        xyz = coords.strip().split(',')
        coordlims = tuple( 
            tuple( int(x) for x in tok.split('=')[1].split('..') )
            for tok in xyz
        )
        instructions.append(instr)
        ranges.append(coordlims)

    cubes = defaultdict(lambda: 0)
    for instr, (xl, yl, zl) in zip(instructions, ranges):
        if max(xl) < -50 or min(xl) > 50 or \
           max(yl) < -50 or min(yl) > 50 or \
           max(zl) < -50 or min(zl) > 50:
            continue
        for x,y,z in product(range(max(-50,xl[0]),min(xl[1],50)+1),
                             range(max(-50,yl[0]),min(yl[1],50)+1),
                             range(max(-50,zl[0]),min(zl[1],50)+1)):
            if instr == 'on':
                cubes[(x,y,z)] = 1
            else:
                cubes[(x,y,z)] = 0


    print('#cubes on: ', sum(cubes.values()))

if __name__ == '__main__':
    main()
