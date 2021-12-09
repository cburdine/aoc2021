#!/bin/env python3

import sys

N_2_SEGS = {
    0 : 'abcefg',
    1 : 'cf',
    2 : 'acdeg',
    3 : 'acdfg',
    4 : 'bcdf',
    5 : 'abdfg',
    6 : 'abdefg',
    7 : 'acf',
    8 : 'abcdefg',
    9 : 'abcdfg'
}

LEN_2_N = {}
for k,v in N_2_SEGS.items():
    if not len(v) in LEN_2_N:
        LEN_2_N[len(v)] = []
    LEN_2_N[len(v)].append(k)

def solve(data, numbers):
    total = 0
    for n in numbers:
        if len(LEN_2_N[len(n)]) == 1:
            total += 1

    return total

def main():
    print(LEN_2_N)
    
    lines = sys.stdin.readlines()
    digits = []
    for line in lines:
        data, numbers = line.split('|')[:2]
        data = [ d.strip() for d in data.strip().split(' ') ]
        numbers = [ n.strip() for n in numbers.strip().split(' ') ]
        digits.append(solve(data, numbers))
    
    print('total: ', sum(digits))

if __name__ == '__main__':
    main()


