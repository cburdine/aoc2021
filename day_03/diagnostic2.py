#!/bin/env python3

import sys

def main():

    lines = [ line.strip() for line in sys.stdin.readlines() ]
    nbits = len(lines[0])
    print('#bits: ', nbits)
    

    o2_lines = lines
    co2_lines = lines

    o2 = 0
    co2 = 0    

    for n in range(nbits):
        
        next_o2_lines = { '0': [], '1': [] }
        next_co2_lines = { '0': [], '1': [] }
        o2 = o2<<1
        co2 = co2<<1        

        for line in o2_lines:
            next_o2_lines[line[n]].append(line)

        for line in co2_lines:
            next_co2_lines[line[n]].append(line)

        if len(next_o2_lines['1']) >= len(next_o2_lines['0']):
            o2 |= 1
            o2_lines = next_o2_lines['1']
        else:
            o2_lines = next_o2_lines['0']
         

        if len(co2_lines) == 1:
            co2 |= len(next_co2_lines['1'])          
        elif len(next_co2_lines['1']) < len(next_co2_lines['0']):
            co2_lines = next_co2_lines['1']
            co2 |= 1
        else:
            co2_lines = next_co2_lines['0']
    
    print('o2: ', o2, f'{o2:b}')
    print('co2: ', co2, f'{co2:b}')
    print('product: ', o2 * co2)
    

if __name__ == '__main__':
    main()
