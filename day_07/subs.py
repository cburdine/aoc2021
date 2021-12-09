#!/bin/env python3

import sys

def main():
    lines = sys.stdin.readlines()
    positions = [ int(x.strip()) for x in lines[0].split(',') ]
    x_min, x_max = min(positions), max(positions)
    
    freqs = [ 0 for _ in range(x_max+1) ]
    costs = [ 0 for _ in range(x_max+1) ]
    
    for p in positions:
        freqs[p] += 1
    
    # compute costs:
    n_lt = 0
    n_ge = len(positions) 
    costs[0] = sum(positions)
    
    for i in range(1,x_max+1):
        n_lt += freqs[i-1]
        n_ge -= freqs[i-1]
        costs[i] = costs[i-1] + n_lt - n_ge

    print(n_lt, n_ge)
    print('cost arr: ')
    #print(costs)

    print('min cost: ', min(costs))
    

if __name__ == '__main__':
    main()
