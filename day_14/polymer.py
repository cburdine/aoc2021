#!/bin/env python3

import re
import sys

def main():
    lines = sys.stdin.readlines()
    base = list(lines[0].strip())
    patterns = {}

    for line in lines[2:]:
        tokens = line.split('->')
        x = tokens[0].strip()
        r = tokens[1].strip()
        patterns[x] = r
   
    for i in range(10): 
        new_base = [base[0]]
        for tup in zip(base[:-1], base[1:]):
            chs = ''.join(tup)
            if chs in patterns:
                new_base.append(patterns[chs])
            new_base.append(chs[1])
        base = new_base
    
    freqs = {}
    for ch in base:
        if ch not in freqs:
            freqs[ch] = 0
        freqs[ch] += 1

    most_freq = max(freqs.values())
    least_freq = min(freqs.values())

    print('max - min: ', most_freq - least_freq)
 
if __name__ == '__main__':
    main()
