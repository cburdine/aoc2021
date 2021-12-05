#!/bin/env python3

import sys

def main():
    x = 0
    y = 0
    aim = 0
    
    for line in sys.stdin.readlines():
        toks = line.split(' ')
        direction = toks[0].strip()
        dist = int(toks[1])
        if direction == 'forward':
            x += dist
            y += dist*aim
        elif direction == 'up':
            aim += dist
        elif direction == 'down':
            aim -= dist

    print('x', x)
    print('y', y)
    print('product: ', x * -y)


if __name__ == '__main__':
    main()
