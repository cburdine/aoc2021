#!/bin/env python3

import sys

def main():
    data = [
        int(d) for d in 
        sys.stdin.readlines()
    ]

    incr = 0
    for i,j in zip(data[:-1],data[1:]):
        if i < j:
            incr += 1

    print('# increments: ', incr)

if __name__ == '__main__':
    main()
