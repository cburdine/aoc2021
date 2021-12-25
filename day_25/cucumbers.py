#!/bin/env python3 

import sys

def step(grid, h,w):
    n_moved = 0
    
    for cht in '>v':   
        next_grid = {}
        for (i,j), ch in grid.items():
            npos = None
            if ch == cht == '>':
                npos = (i,(j+1)%w)
            elif ch == cht == 'v':
                npos = ((i+1)%h,j)
            
            if npos != None and npos not in grid:
                next_grid[(npos)] = ch
                n_moved += 1
            else:
                next_grid[(i,j)] = ch
        
        grid = next_grid
    
    return n_moved, grid

def print_grid(grid,h,w):
    for i in range(h):
        row = [ grid[(i,j)] if (i,j) in grid else '.' 
                for j in range(w) ]
        print(''.join(row))

def main():

    grid = {}
    lines = sys.stdin.readlines()
    h = len(lines)
    w = len(lines[0].strip())
    
    for i, l in enumerate(lines):
        for j, ch in enumerate(l.strip()):
            if ch in 'v>':
                grid[(i,j)] = ch
    
    for n in range(1000000000):
        n_moved, grid = step(grid,h,w)
        print(n, n_moved)

        if n_moved == 0:
            break

    print('#steps:', n+1)

if __name__ == '__main__':
    main()
