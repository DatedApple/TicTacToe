#import copy
import board

def bestMove(board, current):
    ai = current
    return _bestMove(board, current, ai)

def _bestMove(board, current, ai):
    bestScore = int(-1e9)
    placement = [-1, -1]
    for i in range(3):
        for j in range(3):
            if board.board[i][j] == " ":
                board.board[i][j] = current
                score = _bestMove(board, "X", ai) if current == "O" else _bestMove(board, "X", ai)
                if score > bestScore:
                    bestScore = score
                    placement = (i, j)
                board.board[i][j] = " "
    return placement[0] * 3 + placement[1]


