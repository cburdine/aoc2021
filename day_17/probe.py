#!/bin/env python3

import sys

def simulate_trajectory(vx, vy, x_range, y_range):
    x,y = 0,0
    traj = [(0,0)]
    while y >= min(y_range):
        if (x_range[0] <= x <= x_range[1]) and \
           (y_range[0] <= y <= y_range[1]):
            return traj
        x += vx
        y += vy
        if vx != 0:
            vx -= vx//abs(vx)
        vy -= 1
        traj.append((x,y))

    return None

def main():
    lines = sys.stdin.readlines()
    data = lines[0].strip().split(' ')[2:]
    x_tokens = data[0][2:].split('..')
    y_tokens = data[1][2:].split('..')
    
    x_range = tuple(int(x.strip(' ,')) for x in x_tokens)
    y_range = tuple(int(y.strip(' ,')) for y in y_tokens)
    assert(min(x_range) > 0)
 
    max_vy_abs = 2*max(abs(y_range[0]),abs(y_range[1])) + 2*abs(y_range[1] - y_range[0])
    
    trajs = []
    print('vx range: ', (0, max(x_range)))
    print('vy range: ', (-max_vy_abs, max_vy_abs))
     
    for vx in range(max(x_range)+1):
        for vy in range(-max_vy_abs, max_vy_abs+1):
            traj = simulate_trajectory(vx, vy, x_range, y_range)
            if traj != None:
                trajs.append(traj)
           
    print('max height: ', max(max([y for _,y in t]) for t in trajs))

if __name__ == '__main__':
    main()
