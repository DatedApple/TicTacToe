#import copy
import board

def bestMove(board, current):
    bestScore = int(-1e9)
    placement = [-1, -1]
    for i in range(3):
        for j in range(3):
            if board[i][j] == " ":
                board[i][j] = current
                score = minmax(board, current)
                if score > bestScore:
                    bestScore = score
                    placement = [i, j]
                board[i][j] = " "
    return placement[0] * 3 + placement[1]

def minmax(board, curr):
    return 1
