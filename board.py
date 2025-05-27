def board():
    a = [[" ", " ", " "],[" ", " ", " "], [" ", " ", " "]]
    return a

def locator():
    x = 0
    b = board()
    for i in range(3):
        a = b[i]
        for j in range(3):
            a[j] = f"{x}"
            x+=1
        b[i] = a
    boardPrinter(b)


def boardPrinter(brd):
    start = True
    for x in brd:
        if start is False:
            print("-----")
        print("|".join(x))
        start = False
        

def newBoard():
    newBoard = board()
    print("new game beggining...")
    # boardPrinter(newBoard)
    return newBoard

def placeToken(player, coords, brd):
    i = int(coords/3)
    j = coords%3
    brd[i][j] = player

def isFull(brd):
    for x in brd:
        # print("Checking row")
        for y in x:
            # print(y)
            if y == " ":
                return False
    print("Board is full")
    return True

def checkLine(b, p, x):
    for cell in b[x]:
        if cell != p:
            return False
    return True

def checkRow(b, p, y):
    for x in range(3):
        if b[x][y] != p:
            return False
    return True

def checkDiagonal(b, p, x, y):
    leftie = False
    rightie = False
    if x == y:
        leftie = True
        for i in range(3):
            # print(b[i][i])
            if b[i][i] != p:
                leftie = False
                break
    if x+y==2:
        rightie = True
        for i in range(3):
            if b[i][2-i] != p:
                rightie = False
                break
    return leftie or rightie
def checkGame(brd, x, y):
    curr = brd[x][y]
    line = checkLine(brd, curr, x)
    # print(f"line: {line}")
    row = checkRow(brd, curr, y)
    # print(f"row: {row}")
    diagonal = checkDiagonal(brd, curr, x, y)
    # print(f"diag: {diagonal}")
    if line or row or diagonal:
        return curr
    else:
        return None
