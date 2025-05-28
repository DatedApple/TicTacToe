import board

def isInvalid(g, c):
    if isinstance(c, int) is not True:
        print("\n[!] Invalid input: Please enter a number between 0 and 8.\n")
        return True
    if c >= 9 or c < 0:
        print("\n[!] Out of bounds: Please select a number from 0 to 8.\n")
        return True
    i = int(c/3)
    j = c%3
    empty = " "
    if g[i][j] == empty:
        return False
    print("\n[!] That space is already taken. Please choose another.\n")
    return True


def getMove(grid):
    invalid = True
    while(invalid):
        print("\n" + "="*30)
        print("Select a space using the number shown below:")
        board.locator()
        print()
        try:
            c = int(input("\u25B6 Enter your move (0-8): "))
        except ValueError:
            print("\n[!] Invalid input: Please enter a number between 0 and 8.\n")
            continue
        invalid = isInvalid(grid, c)
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
    x = int(c/3)
    y = c%3
    res = board.checkGame(b, x, y)
    return res

def changePlayer(pl):
    print("-"*20)
    print(f"End of {pl}'s turn")
    print("-"*20)
    if pl == "X":
        return "O"
    else:
        return "X"

newGame = True
while(newGame):
    #Create loop (ask player if new game)
    #New board for game
    grid = board.newBoard()
    curr = "X"
    cont = True
    # move(curr, grid)
    #loop instructions for game
    #check ifWinner or smth

    while(cont):

        #make move
        #makeMove will first get the desired position than board to perform the change
        

        #Check for winner
        lastMove = move(curr, grid)
        winner = getWinner(grid, lastMove)
        curr = changePlayer(curr)
        #crowns winner
        if winner is not None:
            print(f"Winner is {winner}")
            cont = False
            break
        full = board.isFull(grid)
        if full is True:
            board.boardPrinter(grid)
            print("Draw")
            cont = False
            break
    invalid = True
    while(invalid):
        ans = input("="*30+"\nStart new game [Y/n]: ")
        if ans != "Y" and ans != "n":
            print("\n[!] Invalid input. Please enter either Y or n only")
        else:
            invalid = False
            if ans == "Y":
                newGame = True
            if ans == "n":
                newGame = False
    print("*"*30)


