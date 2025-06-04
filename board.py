def create_board():
    return [[" "] * 3 for _ in range(3)]

def locator():
    b = [[str(i * 3 + j) for j in range(3)] for i in range(3)]
    boardPrinter(b)


def boardPrinter(brd):
    for idx, row in enumerate(brd):
        print("|".join(row))
        if idx < 2:
            print("-" * 5)
        

def newBoard():
    print("new game beginning...")
    return create_board()

def placeToken(player, coords, brd):
    i, j = divmod(coords, 3)
    brd[i][j] = player

def isFull(brd):
    for row in brd:
        if " " in row:
            return False
    print("Board is full")
    return True

def checkLine(b, p, x):
    return all(cell == p for cell in b[x])

def checkRow(b, p, y):
    return all(b[x][y] == p for x in range(3))

def checkDiagonal(b, p, x, y):
    leftie = x == y and all(b[i][i] == p for i in range(3))
    rightie = x + y == 2 and all(b[i][2 - i] == p for i in range(3))
    return leftie or rightie
def checkGame(brd, x, y):
    curr = brd[x][y]
    if curr == " ":
        return None
    if checkLine(brd, curr, x) or checkRow(brd, curr, y) or checkDiagonal(brd, curr, x, y):
        return curr
    return None
