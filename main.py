import board
import random
import AI.minmax as mn

def is_invalid_move(grid, coord):
    if not isinstance(coord, int):
        print("\n[!] Invalid input: Please enter a number between 0 and 8.\n")
        return True
    if coord < 0 or coord >= 9:
        print("\n[!] Out of bounds: Please select a number from 0 to 8.\n")
        return True
    i, j = divmod(coord, 3)
    if grid[i][j] == " ":
        return False
    print("\n[!] That space is already taken. Please choose another.\n")
    return True


def getMove(grid):
    while True:
        print("\n" + "="*30)
        print("Select a space using the number shown below:")
        board.locator()
        print()
        try:
            c = int(input("\u25B6 Enter your move (0-8): "))
        except ValueError:
            print("\n[!] Invalid input: Please enter a number between 0 and 8.\n")
            continue
        if not is_invalid_move(grid, c):
            print("="*30 + "\n")
            return c

def move(curr, grid):
    print(f"\n{'*'*10} Player {curr}'s Turn {'*'*10}")
    coords = getMove(grid)
    board.placeToken(curr, coords, grid)
    print("\nCurrent Board:")
    board.boardPrinter(grid)
    return coords

def getWinner(b, c):
    x, y = divmod(c, 3)
    return board.checkGame(b, x, y)

def changePlayer(pl):
    print("-"*20)
    print(f"End of {pl}'s turn")
    print("-"*20)
    return "O" if pl == "X" else "X"

def aiMove(grid, curr):
    lastMove = mn.bestMove(grid, curr)
    board.placeToken(curr, lastMove, grid)

def start():
    print("*"*31)
    print("*"+" "*29+"*")
    print("*"+" "*9+"TIC TAC TOE"+" "*9+"*")
    print("*"+" "*29+"*")
    print("*"*31)
    response = int(input("\t 1 player mode OR 2 player mode (1/2):\t"))
    return True if response == 2 else False

def main():
    xScore = 0
    oScore = 0
    newGame = True
    twoPlayer = start()
    while newGame:
        grid = board.newBoard()
        curr = "X"
        cont = True
        lastMove = None
        while cont:
            if curr == "X" or twoPlayer:
                lastMove = move(curr, grid)
                curr = changePlayer(curr)
            else:
                print(f"\n{'*'*10} Player {curr} (AI) is thinking... {'*'*10}")
                lastMove = aiMove(grid, curr)
            winner = getWinner(grid, lastMove)
            if winner is not None:
                print(f"Winner is {winner}")
                if winner == "X":
                    xScore += 1
                else:
                    oScore += 1
                print(f"Score: X = {xScore}, O = {oScore}")
                cont = False
                break
            if board.isFull(grid):
                board.boardPrinter(grid)
                print("Draw")
                cont = False
                break
        while True:
            ans = input("="*30+"\nStart new game [Y/n]: ")
            if ans not in ("Y", "n"):
                print("\n[!] Invalid input. Please enter either Y or n only")
            else:
                newGame = (ans == "Y")
                break
        print("*"*30)
        print(f"\tFinal score\nO:{oScore}\tX:{xScore}\n"+"="*30+"\tEnding game...")

if __name__ == "__main__":
    main()


