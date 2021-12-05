#!/bin/env python3

import sys

def main():

    lines = sys.stdin.readlines()
    bit_counts = [ 0 for _ in lines[0].strip() ]
    print('#bits: ', len(bit_counts))

    for line in lines: 
        for i, bit in enumerate(line.strip()):
            if int(bit):
                bit_counts[i] += 1
            else:
                bit_counts[i] -= 1
    
    eps = 0
    gamma = 0

    for cnt in bit_counts:
        gamma = (gamma<<1)
        eps = (eps<<1)
        if cnt > 0:
            gamma |= 1
        else:
            eps |= 1
    
    print(bit_counts)
    print('gamma: ', gamma)
    print('epsilon: ', eps)
    print('product: ', gamma*eps)

if __name__ == '__main__':
    main()
