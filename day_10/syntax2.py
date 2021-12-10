#!/bin/env python3

import sys

OPEN_SYMBOLS = '([{<'
CLOSE_SYMBOLS = ')]}>'

ERR_PTS = {
    ')' : 3,
    ']' : 57,
    '}' : 1197,
    '>' : 25137
}

ERR_MULTS = {
    ')': 1,
    ']': 2,
    '}': 3,
    '>': 4
}

def main():
    
    lines = sys.stdin.readlines()
    scores = []
    for i, line in enumerate(lines):
        stk = []
        for ch in line.strip():
            if ch in OPEN_SYMBOLS:
                idx = OPEN_SYMBOLS.index(ch)
                stk.append(CLOSE_SYMBOLS[idx])
            elif ch in CLOSE_SYMBOLS:
                if stk[-1] != ch:
                    break
                else:
                    stk.pop()
        else:
            score = 0
            for ch in reversed(stk):
                score *= 5
                score += ERR_MULTS[ch]
            
            print(f'line[{i}]: ', score)
            scores.append(score)
        
    scores.sort()
    idx = len(scores)//2
    
    print('middle score: ', scores[idx])

if __name__ == '__main__':
    main()
