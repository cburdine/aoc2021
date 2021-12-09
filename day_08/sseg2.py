#!/bin/env python3

import sys
import itertools

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

SEGS_2_N = { v : k for k,v in N_2_SEGS.items() }

def solve(data, numbers):
    target_maps = set(N_2_SEGS.values())
    segmap = None
    for perm in itertools.permutations('abcdefg'):
        segmap = { ch  : perm[i] for i, ch in enumerate('abcdefg') }
        
        # check validity of segmap:
        mapped_segs = set( ''.join(sorted([segmap[ch] for ch in d])) for d in data )
        if mapped_segs == target_maps:
            break
    else:
        raise 'no valid mapping!'

    print(segmap)
    
    decoded_vals = [
        SEGS_2_N[''.join(sorted([ segmap[ch] for ch in n ]))]
        for n in numbers
    ]
    
    result = 0
    for d in decoded_vals:
        result = result*10 + d

    print(result)
    return result

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


