class Board:
    def _init_(self):
        self.board = [[" "] * 3 for _ in range(3)]

    def locator(self):
        b = [[str(i * 3 + j) for j in range(3)] for i in range(3)]
        self.boardPrinter(b)

    def printer(self):
        self.boardPrinter(self.board)

    def boardPrinter(self, brd):
        for idx, row in enumerate(brd):
            print("|".join(row))
            if idx < 2:
                print("-" * 5)
            

    def newBoard(self):
        print("new game beginning...")
        return self.create_board()

    def placeToken(self, player, coords):
        i, j = divmod(coords, 3)
        self.board[i][j] = player

    def isFull(self):
        for row in self.board:
            if " " in row:
                return False
        print("Board is full")
        return True

    def checkLine(self, p, x):
        return all(cell == p for cell in self.board[x])

    def checkRow(self, p, y):
        return all(self.board[x][y] == p for x in range(3))

    def checkDiagonal(self, p, x, y):
        leftie = x == y and all(self.board[i][i] == p for i in range(3))
        rightie = x + y == 2 and all(self.board[i][2 - i] == p for i in range(3))
        return leftie or rightie
    
    def checkGame(self):
        for x in range(3):
            for y in range(3):
                curr = self.board[x][y]
                if curr == " ":
                    return None
                if self.checkLine(curr, x) or self.checkRow(curr, y) or self.checkDiagonal(curr, x, y):
                    return curr
                return None
