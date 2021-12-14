#!/bin/env python3


import sys
from collections import defaultdict

def main():
    lines = sys.stdin.readlines()
    base = list(lines[0].strip())
    patterns = {} 

    for line in lines[2:]:
        tokens = line.split('->')
        x = tokens[0].strip()
        r = tokens[1].strip()
        patterns[(x[0],x[1])] = r
   
    pair_freqs = defaultdict(lambda: 0)
    freqs = defaultdict(lambda: 0)

    for ch in base:
        freqs[ch] += 1

    for pair in zip(base[:-1],base[1:]):
        pair_freqs[pair] += 1

    for i in range(40): 
        new_pair_freqs = defaultdict(lambda: 0)
        for pair, n in pair_freqs.items():
            if pair in patterns:
                ch = patterns[pair]
                new_pair_freqs[(pair[0],ch)] += n
                new_pair_freqs[(ch,pair[1])] += n
                freqs[ch] += n
            else:
                new_pair_freqs[pair] += n
        pair_freqs = new_pair_freqs
    
    most_freq = max(freqs.values())
    least_freq = min(freqs.values())

    print('max - min: ', most_freq - least_freq)
 
if __name__ == '__main__':
    main()
