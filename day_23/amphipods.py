#!/bin/env python3

import sys

HALL_X = [ 0,1,3,5,7,9,10,11]
ROOM_X = [ 2, 4, 6, 8 ]

COSTS = [ 1, 10, 100, 1000 ]


def dist(p0,p1):
    x0,y0 = p0
    x1,y1 = p1
    return abs(x0-x1)+abs(y0-y1)

def state_str(state):
    g = [ list(s) for s in (
"""#############
#...........#
###.#.#.#.###
  #.#.#.#.#
  #########
""").split('\n') ]
    
    for pos in state:
        x,y = pos
        key, done = state[pos]
        if done:
            g[y+1][x+1] = chr(ord('a')+key)
        else:
            g[y+1][x+1] = chr(ord('A')+key)    
    return '\n'.join([''.join(s) for s in g ])
        

def valid_moves(state, pos):
    assert(pos in state)
    x0,y0 = pos
    key, done = state[pos]
    rx = ROOM_X[key]

    if done:
        return []
    
    moves = []
    costs = []
     
    # handle moving from hallway:
    if y0 == 0 and (rx,1) not in state:
        pr1 = (rx,1)
        pr2 = (rx,2)
        if path_exists(pos,pr2,state):
            moves.append(pr2)
            costs.append(dist(pos,pr2)*COSTS[key])
        elif pr2 in state and state[pr2] == (key,True) and \
            path_exists(pos,pr1,state):
            moves.append(pr1)
            costs.append(dist(pos,pr1)*COSTS[key])
    
    # handle moving into hallway:
    elif y0 > 0:
        # handle blocking room exit:
        if y0 == 2 and (x0,1) in state:
            return []
        
        for x1 in HALL_X:
            ph = (x1,0)
            if path_exists(pos,ph,state):
                moves.append(ph)
                costs.append(dist(pos,ph)*COSTS[key])
        
    return sorted(list(zip(moves, costs)), key=lambda x: x[1])
    
def path_exists(pos0, pos1, state):
    assert(pos0 in state)

    if pos0 == pos1 or pos1 in state:
        return False
    
    room_pos = pos0 if pos0[1] > 0 else pos1
    hall_pos = pos0 if pos0[1] == 0 else pos1
    hx, hy = hall_pos
    rx, ry = room_pos
    for x in HALL_X:
        if min(rx,hx) <= x <= max(rx,hx) and \
            (x,0) != pos0 and (x,0) in state:
                return False
    
    if ry == 2 and (rx,1) in state:
        return False
    
    return True


def compute_cost(state, cache={}):

    cache_key = tuple(sorted(state.items()))
    if cache_key in cache:
        return cache[cache_key]
    
    n_done = sum(int(v) for _,v in state.values())
    n_moving = sum(1 for p in state if p[1] == 0)
    
    #print(len(m), n_done, n_moving)
    #print(state_str(state))
     
    if n_done >= len(state):
        return 0, []

    min_cost = None 
    min_moves = None
    for pos in state:
        key, done = state[pos]
        if not done:
            moves = valid_moves(state, pos)
            for next_pos, c in moves:
                if min_cost != None and min_cost < c:
                    break
                
                new_state = state.copy()
                new_state.pop(pos)
                new_state[next_pos] = (key,next_pos[1] > 0)
                c2, m2 = compute_cost(new_state, cache)
                
                if c2 != None:
                    if min_cost == None:
                        min_cost = c+c2
                        min_moves = [(pos,next_pos,c)] + m2
                    elif min_cost > c+c2:
                        min_cost = min(min_cost, c+c2)
                        min_moves = [(pos,next_pos,c)] + m2
         
        cache[cache_key] = min_cost, min_moves
    return min_cost, min_moves
                

def main():
    lines = sys.stdin.readlines()
    state = {}
    for y in range(3):
        for x, ch in enumerate(lines[y+1][1:]):
            if ch in 'ABCD':
                assert(x in ROOM_X)
                key = ord(ch) - ord('A')
                done = (ROOM_X.index(x) == key) and \
                       (y == 2 or (y == 1 and lines[y+2][x+1] == ch))
                state[(x,y)] = (key,done)
    
    min_cost, moves = compute_cost(state)
    print(state_str(state))
    for src, dest,c in moves:
        key, done = state.pop(src)
        if dest[1] > 0:
            done = True
        state[dest] = (key,done)
        print('cost:', c)
        print(state_str(state))
    print('total cost: ', sum(m[2] for m in moves))        



if __name__ == '__main__':
    main()
