#!/bin/env python3

import sys

def main():
    fish = [ 
        int(x.strip()) for x in 
        sys.stdin.readlines()[0].split(',')
    ]

    timers = [ 0 for _ in range(9) ]
    for f in fish:
        timers[f] += 1

    nsteps = 80
    for s in range(nsteps):
        new_fish = timers[0]
        for i in range(8):
            timers[i] = timers[i+1]
        timers[6] += new_fish
        timers[8] = new_fish

        print(s, timers)

    print('total: ', sum(timers))

if __name__ == '__main__':
    main()
            
