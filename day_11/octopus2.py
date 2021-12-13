#!/bin/env python3

import sys

def step(grid):
    n_flashes = 0
    flashes = []
    for pos in grid:
        grid[pos] += 1
        if grid[pos] > 9:
            grid[pos] = 0
            n_flashes += 1
            flashes.append(pos)
    
    while flashes:
        new_flashes = []
        for pos in flashes:
            i,j = pos
            for pos2 in [(i-1,j),(i+1,j),(i,j-1),(i,j+1),
                         (i-1,j-1),(i+1,j-1),(i-1,j+1),(i+1,j+1)]:
                if pos2 in grid and grid[pos2]:
                    grid[pos2] += 1
                    if grid[pos2] > 9:
                        grid[pos2] = 0
                        n_flashes += 1
                        new_flashes.append(pos2)
        
        flashes = new_flashes
    return n_flashes

def print_grid(grid):
    h = max(k[0] for k in grid.keys()) + 1
    w = max(k[1] for k in grid.keys()) + 1
    for i in range(h):
        print(''.join([ 
            str(grid[(i,j)]) for j in range(w)
        ]))
    print('----')
             
def main():
    lines = sys.stdin.readlines()
    grid = { 
        (i,j) : int(x) 
        for i, line in enumerate(lines)
        for j, x in enumerate(line.strip())
    }
    n_steps = 1
    n_elems = len(grid)
    
    print_grid(grid)
    while step(grid) != n_elems:
        n_steps += 1

    print_grid(grid)
    print('# steps: ', n_steps)

if __name__ == '__main__':
    main()
