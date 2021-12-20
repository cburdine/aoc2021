#!/bin/env python3

import sys

NEIGHBOR_ORDER = [
    (-1,-1), (-1,0),  (-1,1),
    (0,-1),  (0,0),   (0,1),
    (1,-1),  (1,0),   (1,1)
]

def print_grid(grid):
    i_rng = min(k[0] for k in grid), max(k[0] for k in grid) 
    j_rng = min(k[1] for k in grid), max(k[1] for k in grid)
    
    for i in range(i_rng[0],i_rng[1]+1):
        print(''.join([
            '#' if (i,j) in grid else '.'
            for j in range(j_rng[0],j_rng[1]+1)
        ]))
            
def enhance(grid, alg, background=False):
    new_grid = set()
    new_background = alg[(1<<9)-1] if background else alg[0]
    grid_neighbors = set(
        (i+di,j+dj)
        for (i,j) in grid
        for di,dj in NEIGHBOR_ORDER
    )
    
    for (i,j) in grid_neighbors:
        idx = 0
        for di,dj in NEIGHBOR_ORDER:
            idx = (idx<<1)
            if (i+di,j+dj) in grid:
                idx |= 1
        if background:
            idx = (~idx)&((1<<9)-1)
        
        if alg[idx] != new_background:
            new_grid.add((i,j)) 
    
    return new_grid, new_background

def main():
    lines = sys.stdin.readlines()
    alg = [ True if c == '#' else False 
            for c in lines[0].strip() ]
    assert(len(alg) == 1<<9)
    
    grid = set()
    background = False
    
    assert(len(lines[1].strip()) == 0) 
    
    for i, l in enumerate(lines[2:]):
        for j, c in enumerate(l.strip()):
            assert(c in ['.','#'])
            if c == '#':
                grid.add((i,j))

    for _ in range(2):
        grid, background = enhance(grid, alg, background)
    
    print_grid(grid)  
    print('#pixels lit: ', len(grid))

if __name__ == '__main__':
    main()
