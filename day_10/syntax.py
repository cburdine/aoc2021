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

def main():
    
    lines = sys.stdin.readlines()
    score = 0
    for line in lines:
        stk = []
        for ch in line.strip():
            if ch in OPEN_SYMBOLS:
                idx = OPEN_SYMBOLS.index(ch)
                stk.append(CLOSE_SYMBOLS[idx])
            elif ch in CLOSE_SYMBOLS:
                if stk[-1] != ch:
                    score += ERR_PTS[ch]
                    break
                else:
                    stk.pop()

    print('score: ', score)

if __name__ == '__main__':
    main()
