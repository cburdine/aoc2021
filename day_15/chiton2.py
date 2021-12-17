#!/bin/env python3

import sys
from itertools import product
from heapq import heappush, heappop

def dijkstra(graph, start, end=None):
    """graph[v0] = (v1,dist)"""
    D = { start: 0 }
    P = { start: start }
    Q = [ (0,start) ]
     
    while Q:
        p, v = heappop(Q)
        if v == end:
            break
        for (nv, d) in graph[v]:
            nd = d + D[v]
            if nv not in D or nd < D[nv]:
                heappush(Q,(nd, nv))
                D[nv] = nd
                P[nv] = v
    
    return D, P
                

def main():
    lines = sys.stdin.readlines()
    h = len(lines)
    w = len(lines[0].strip())
    grid = {
        (i,j): int(x)
        for i, line in enumerate(lines)
        for j, x in enumerate(line.strip())
    }
        
    end = (5*h-1,5*w-1)
    for dh, dw in product(range(0,5),range(0,5)):
        for i, j in product(range(h),range(w)):
            pos = (i+dh*h,j+dw*w)
            grid[pos] = 1+((dh+dw+grid[(i,j)]-1)%9)
     
    graph = { pos : [] for pos in grid }
    for pos in grid:
        i, j = pos
        for npos in [(i-1,j),(i+1,j),(i,j-1),(i,j+1)]:
            if npos in grid:
                graph[pos].append((npos,grid[npos]))
  
    dists, _ = dijkstra(graph, start=(0,0),end=end)
    print('risk: ', dists[end])

if __name__ == '__main__':
    main()
