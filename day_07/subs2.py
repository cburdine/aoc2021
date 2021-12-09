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
    costs[0] = sum([ p*(p+1)//2 for p in positions ])
    n_positions = len(positions)
    positions_sum = sum(positions)    
 
    for i in range(1,x_max+1):
        costs[i] = sum( abs(x-i)*(abs(x-i)+1)//2 for x in positions ) 

    print('cost arr: ')
    print(costs)

    print('min cost: ', min(costs))
    

if __name__ == '__main__':
    main()
