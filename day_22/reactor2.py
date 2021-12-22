#!/bin/env python3

import sys
from collections import defaultdict
from itertools import product

def cube_volume(c):
    xl,yl,zl = c
    return (1+xl[1]-xl[0])*(1+yl[1]-yl[0])*(1+zl[1]-zl[0])

def cube_intersects(c1, c2):
    (xl1,yl1,zl1) = c1
    (xl2,yl2,zl2) = c2
    return (max(xl1[0],xl2[0]) <= min(xl1[1],xl2[1])) and \
           (max(yl1[0],yl2[0]) <= min(yl1[1],yl2[1])) and \
           (max(zl1[0],zl2[0]) <= min(zl1[1],zl2[1]))

def subtract_cubes(c2, c1):
    # return list of cubes representing c2 - c1:    
    range_options = []
    for l1, l2 in zip(c1, c2):
        ax_options = []
        if l2[0] <= min(l2[1],l1[0]-1):
            ax_options.append((l2[0],min(l2[1],l1[0]-1)))
        if max(l1[0],l2[0]) <= min(l1[1],l2[1]):
           ax_options.append(
            (max(l1[0],l2[0]),min(l1[1],l2[1]))
           )
        if max(l1[1]+1,l2[0]) <= l2[1]:
            ax_options.append((max(l1[1]+1,l2[0]),l2[1]))
        
        range_options.append(ax_options)
    
    subcubes = product(*range_options)
    return [ c for c in subcubes if not cube_intersects(c,c1) ] 

def main():

    lines = sys.stdin.readlines()
    
    instructions = []
    inst_cubes = []
    for line in lines:
        instr, coords = line.strip().split(' ')
        xyz = coords.strip().split(',')
        cube = tuple( 
            tuple( int(x) for x in tok.split('=')[1].split('..') )
            for tok in xyz
        )
        instructions.append(instr)
        inst_cubes.append(cube)
    
    on_cubes = []
    for instr, c1 in zip(instructions, inst_cubes):
        new_on_cubes = []
        for c2 in on_cubes:
            if cube_intersects(c2,c1):
                new_on_cubes.extend(subtract_cubes(c2,c1))
            else:
                new_on_cubes.append(c2)
        if instr == 'on':
            new_on_cubes.append(c1)
        else:
            assert(instr == 'off')
        on_cubes = new_on_cubes
        
    print('#cubes on: ', sum(cube_volume(c) for c in on_cubes))

if __name__ == '__main__':
    main()
