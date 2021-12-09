#!/bin/env python3

import sys

def main():
    lines = sys.stdin.readlines()
    grid = [[ int(x) for x in l.strip() ] for l in lines ]
    h = len(grid)
    w = len(grid[0])

    low_pts = {}

    for i in range(h):
        for j in range(w):
            if ((i <= 0)   or (grid[i-1][j] > grid[i][j])) and \
               ((i+1 >= h) or (grid[i+1][j] > grid[i][j])) and \
               ((j <= 0)   or (grid[i][j-1] > grid[i][j])) and \
               ((j+1 >= w) or (grid[i][j+1] > grid[i][j])):
                    low_pts[(i,j)] = grid[i][j]+1

    print('sum: ', sum(low_pts.values())) 

if __name__ == '__main__':
    main()
