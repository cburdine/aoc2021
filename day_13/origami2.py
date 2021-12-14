#!/bin/env python3

import sys

def fold(dots, axis, val):
    for (x,y) in dots.copy():
        if axis == 'y' and y >= val:
            assert(y != val)
            dots.pop((x,y))
            new_dot = (x,val-(y-val))
            if new_dot not in dots:
                dots[new_dot] = 0
            dots[new_dot] += 1
        elif axis == 'x' and x >= val:
            assert(x != val)
            dots.pop((x,y))
            new_dot = (val-(x-val),y)
            if new_dot not in dots:
                dots[new_dot] = 0
            dots[new_dot] += 1

def print_dots(dots):
    xm, ym = max(k[0] for k in dots), max(k[1] for k in dots)
    print('\n'.join([
        ''.join([
            '#' if (x,y) in dots else ' '
            for x in range(xm+1)
        ]) for y in range(ym+1)
    ]))

def main():
    lines = sys.stdin.readlines()
    dots = {}
    folds = []

    for i, line in enumerate(lines):
        if len(line.strip()) > 0:
            tokens = line.strip().split(',')
            x, y = int(tokens[0]), int(tokens[1])
            dots[(x,y)] = 1
        else:
            for l in lines[i+1:]:
                tokens = l.strip().split('=')
                axis = tokens[0][-1]
                val = int(tokens[1])
                folds.append((axis,val))
            break

    for axis, val in folds:
        fold(dots, axis, val)
        print('#dots: ', len(dots))
    
    print_dots(dots)

if __name__ == '__main__':
    main()
