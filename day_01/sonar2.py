#!/bin/env python3

import sys

def main():
    data = [
        int(d) for d in 
        sys.stdin.readlines()
    ]

    sums = [ 
        (i+j+k) for i,j,k in
        zip(data[:-2],data[1:-1],data[2:])
    ]

    incr1, incr2 = 0, 0
    for i,j in zip(data[:-1],data[1:]):
        if i < j:
            incr1 += 1

    for i,j in zip(sums[:-1],sums[1:]):
        if i < j:
            incr2 += 1

    print('# increments (1): ', incr1)
    print('# increments (2): ', incr2)

if __name__ == '__main__':
    main()
