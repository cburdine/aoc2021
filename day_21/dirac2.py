#!/bin/env python3

import sys
from itertools import product

def compute_distributions(state, cache={}):
    if state in cache:
        return cache[state]

    p_pos, p_score, o_pos, o_score = state
    
    if o_score >= 21:
        return (0,1)
    
    n_wins = 0
    n_losses = 0
    
    for dicevals in product([1,2,3],[1,2,3],[1,2,3]):
        new_p_pos = ((p_pos + sum(dicevals) - 1)%10)+1
        new_p_score = p_score + new_p_pos
        new_state = (o_pos, o_score, new_p_pos, new_p_score)
        o_wins, o_losses = compute_distributions(new_state, cache)
        n_wins += o_losses
        n_losses += o_wins
    
    cache[state] = (n_wins, n_losses)
    return (n_wins, n_losses)


def main():
    lines = sys.stdin.readlines()
    positions = [
        int(lines[i].split(' ')[-1].strip())
        for i in [0,1]
    ]

    init_state = (positions[0],0,positions[1],0)
    result = compute_distributions(init_state)
    print('player 1 wins:', result[0])
    print('player 2 wins:', result[1])
    print('winning universes: ', max(result))

if __name__ == '__main__':
    main()
