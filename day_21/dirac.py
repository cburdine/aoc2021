#!/bin/env python3

import sys

_dice = 0

def dice():
    global _dice
    val = (_dice % 100) + 1
    _dice += 1
    return val

def main():
    lines = sys.stdin.readlines()
    positions = [
        int(lines[i].split(' ')[-1].strip())
        for i in [0,1]
    ]
    
    score = { i : 0 for i, _ in enumerate(positions)}
    board = { i : pos for i, pos in enumerate(positions) }
    
    while max(score.values()) < 1000:
        for p, pos in board.items():
            dist = dice() + dice() + dice()
            new_pos = (((pos + dist)-1)%10)+1
            score[p] += new_pos
            board[p] = new_pos

            if score[p] >= 1000:
                break            

    losing_score = min(score.values())
    print('losing score: ', losing_score)
    print('#dice rolls: ', _dice)
    print('result: ', losing_score*_dice)
    
    
if __name__ == '__main__':
    main()
