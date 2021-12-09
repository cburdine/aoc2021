#!/bin/env python3

from pprint import pprint
import sys

def main():

    lines = sys.stdin.readlines()
    vents = {}

    for line in lines:
        pairs = line.strip().split('->')
        p1 = pairs[0].split(',')
        p2 = pairs[1].split(',')

        pt = [int(x.strip()) for x in p1 + p2 ]

        if (pt[0] == pt[2]):
            x,y0,y1 = pt[0], min(pt[1],pt[3]), max(pt[1],pt[3])
            for y in range(y0,y1+1):
                if (x,y) not in vents:
                    vents[(x,y)] = 0
                vents[(x,y)] += 1
        elif (pt[1] == pt[3]):
            x0,x1,y = min(pt[0],pt[2]),max(pt[0],pt[2]),pt[1]
            for x in range(x0,x1+1):
                if (x,y) not in vents:
                    vents[(x,y)] = 0
                vents[(x,y)] += 1
        else:
            x0,x1 = pt[0], pt[2]
            dx = 1 if x0 <= x1 else -1
            y0,y1 = pt[1], pt[3]
            dy = 1 if y0 <= y1 else -1
            for x,y in zip(range(x0,x1+dx,dx),range(y0,y1+dy,dy)):
                if (x,y) not in vents:
                    vents[(x,y)] = 0
                vents[(x,y)] += 1
    
    n_crosses = 0
    max_x = max([ c[0] for c in vents.keys()])
    max_y = max([ c[1] for c in vents.keys()])
   
    #arr = [
    #    [ str(vents[(x,y)]) if (x,y) in vents else '.' for x in range(max_x+1) ]
    #    for y in range(max_y+1)
    #]
    #pprint(arr)
 
    for coord, n in vents.items():
        if n > 1:
            n_crosses += 1
        
    print('# crosses: ', n_crosses)


if __name__ == '__main__':
    main() 
