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

    basin_ds = { lp : lp  for lp in low_pts }
    basin_counts = { lp : 1 for lp in low_pts }
    added_elems = low_pts.keys()

    def ds_find(p):
        while p != basin_ds[p]:
            p = basin_ds[p]
        return p

    while added_elems:
        new_added_elems = []
        for i,j in added_elems:
            if (i > 0) and (i-1,j) not in basin_ds and (grid[i-1][j] != 9):
                new_added_elems.append((i,j,i-1,j))
            if (i+1 < h) and (i+1,j) not in basin_ds and (grid[i+1][j] != 9):
                new_added_elems.append((i,j,i+1,j))
            if (j > 0) and (i,j-1) not in basin_ds and (grid[i][j-1] != 9):
                new_added_elems.append((i,j,i,j-1))
            if (j+1 < w) and (i,j+1) not in basin_ds and (grid[i][j+1] != 9):
                new_added_elems.append((i,j,i,j+1))

        added_elems = []
        for (i0,j0,i1,j1) in new_added_elems:
            rep_0 = ds_find((i0,j0))
            if (i1,j1) not in basin_ds:
                basin_ds[(i1,j1)] = rep_0
                basin_counts[rep_0] += 1
                added_elems.append((i1,j1))
            else:
                rep_1 = ds_find((i1,j1))
                if rep_1 != rep_0:
                    # merge basins:
                    bc0 = basin_counts[rep_0]
                    bc1 = basin_counts[rep_1]
                    if bc0 > bc1:
                        basin_ds[rep_1] = basin_ds[rep_0]
                        basin_counts[rep_1] += basin_counts[rep_0]
                        basin_counts[rep_0] = 0
                    else:
                        basin_ds[rep_0] = basin_ds[rep_1]
                        basin_counts[rep_0] += basin_counts[rep_1]
                        basin_counts[rep_1] = 0

        

    print(basin_counts)
    counts = sorted(basin_counts.values(), reverse=True)
    print(counts)

    prod = 1
    for x in counts[:3]:
        prod *= x

    print('Prod of 3 largest Basins: ', prod)

if __name__ == '__main__':
    main()
