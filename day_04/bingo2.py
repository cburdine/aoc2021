#!/bin/env python3

import sys
from pprint import pprint

def winning_board(board):
    hsum = [0 for _ in range(5)]
    vsum = [0 for _ in range(5)]
    for i in range(5):
        for j in range(5):
            hsum[i] += board[i][j]
            vsum[j] += board[i][j]

    dsum = 0
    adsum = 0
    #dsum = sum([board[i][i] for i in range(5)])
    #adsum = sum([board[i][4-i] for i in range(5)])
    
    return (min(min(hsum),min(vsum),dsum, adsum) <= -5)

def score_board(board):
    score = 0
    for row in board:
        for x in row:
            if x > 0:
                score += x
    return score

def add_number(board, n):
    for i in range(5):
        for j in range(5):
            if n == board[i][j]:
                board[i][j] = -1

def main():
    lines = sys.stdin.readlines()
    numbers = [ int(t.strip()) for t in lines[0].split(',') ]

    boards = []
    winner = None
    score = None
    lastnum = None

    for i in range(1,len(lines),6):
        board = [
            [ int(t.strip()) for t in line.split(' ') if t ]  
            for line in lines[i+1:i+6]
        ]
        boards.append(board)
        

    for n in numbers:
        next_boards = []
        for i, board in enumerate(boards):
            add_number(board, n)
            lastnum = n
            
            if winning_board(board):
                score = score_board(board)
            else:
                next_boards.append(board)
        
        boards = next_boards
        print(n, '---------------------------')
        for board in boards:
            pprint(board)

            
 
    print('score: ', score)
    print('round: ', lastnum)
    print('product: ', score*lastnum)

if __name__ == '__main__':
    main()
