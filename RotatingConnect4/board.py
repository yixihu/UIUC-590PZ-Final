class Board:
    def __init__(self):
        self.width = 6
        self.height = 6
        self.board = []
        self.gameOver = False
        self.winningCoin = 0

        for i in range(self.height):
            temp = []
            for j in range(self.width):
                temp.append(0)
            self.board.append(temp)

    def setBoard(self, board2):
        for i in range(self.height):
            for j in range(self.width):
                self.board[i][j] = board2[i][j]

    def put(self, coin, index):
        if index < 0 or index >= self.width:
            return False
        else:
            if self.board[0][index] != 0:
                return False
            for i in reversed(range(6)):
                if self.board[i][index] == 0:
                    self.board[i][index] = coin
                    break
            return True

    def rotate(self, clockWise: True):
        # helper function to get row with occupied slots
        def getRows(board):
            rows = []
            height = len(board)
            width = len(board[0])
            for i in range(height):
                row = []
                for j in range(width):
                    if board[i][j] != 0:
                        row.append(board[i][j])
                rows.append(row)
            return rows

        rows = getRows(self.board)
        afterRotation = []
        for i in range(self.height):
            temp = []
            for j in range(self.width):
                temp.append(0)
            afterRotation.append(temp)

        if clockWise:
            # rotate clockWise 90 degree
            for i in range(self.width):
                tempRow = rows[-1 - i]
                if len(tempRow) != 0:
                    for j in range(len(tempRow)):
                        afterRotation[-1 - j][i] = tempRow[-1 - j]
        else:
            # rotate counter-clockWise 90 degree
            for i in range(self.width):
                tempRow = rows[i]
                if len(tempRow) != 0:
                    for j in range(len(tempRow)):
                        afterRotation[-1 - j][i] = tempRow[j]
        self.setBoard(afterRotation)
        return

    def checkOver(self):
        for i in range(self.height):
            for j in range(self.width):
                try:
                    if self.board[i][j] == self.board[i][j + 1] == self.board[i][j + 2] == self.board[i][j + 3] != 0 \
                            or self.board[i][j] == self.board[i + 1][j] == self.board[i + 2][j] == self.board[i + 3][j] != 0 \
                            or self.board[i][j] == self.board[i + 1][j + 1] == self.board[i + 2][j + 2] == self.board[i + 3][j + 3] != 0 \
                            or self.board[i][j] == self.board[i - 1][j - 1] == self.board[i - 2][j - 2] == self.board[i - 3][j - 3] != 0:
                        self.winningCoin = self.board[i][j]
                        return True
                except IndexError:
                    pass
        return False

    def printBoard(self):
        # print out the board
        for i in range(self.height):
            print("-" * (4 * (self.width) + 1))
            for j in range(self.width):
                print("| " + str(self.board[i][j]), end=" ")
                if j == self.width - 1:
                    print("|")
        print("-" * (4 * (self.width) + 1))

    #############################################################
    # What's in between would be functions for regular Connect4 #
    #############################################################
    def heuristic(self, board, coin: 1):
        value = 0
        for i in range(board.height):
            for j in range(board.width):
                try:
                    # horizontally check connected coins
                    if board[i][j] == board[i][j + 1] == coin:
                        value += 1
                    if board[i][j] == board[i][j + 1] == board[i][j + 2] == coin:
                        value += 50
                    if board[i][j] == board[i][j + 1] == board[i][j + 2] == board[i][j + 3] == coin:
                        value += 10000
                except IndexError:
                    pass

                try:
                    # vertically check connected coins
                    if board[i][j] == board[i + 1][j] == coin:
                        value += 1
                    if board[i][j] == board[i + 1][j] == board[i + 2][j] == coin:
                        value += 50
                    if board[i][j] == board[i + 1][j] == board[i + 2][j] == board[i + 3][j] == coin:
                        value += 10000
                except IndexError:
                    pass

                # diagonally check connected coins
                try:
                    if board[i][j] == board[i + 1][j + 1] == coin:
                        value += 1
                    if board[i][j] == board[i + 1][j + 1] == board[i + 2][j + 2] == coin:
                        value += 50
                    if board[i][j] == board[i + 1][j + 1] == board[i + 2][j + 2] == board[i + 3][j + 3] == coin:
                        value += 10000
                except IndexError:
                    pass

                try:
                    if board[i][j] == board[i - 1][j - 1] == coin:
                        value += 1
                    if board[i][j] == board[i - 1][j - 1] == board[i - 2][j - 2] == coin:
                        value += 50
                    if board[i][j] == board[i - 1][j - 1] == board[i - 2][j - 2] == board[i - 3][j - 3] == coin:
                        value += 10000
                except IndexError:
                    pass

        return value

    def miniMax(self, node, depth, max):
        return
    #############################################################


board = Board()
board.put(1, 2)
board.put(2, 2)
board.put(1, 1)
board.put(2, 3)
board.put(1, 1)
board.put(2, 1)
board.put(1, 3)
board.put(2, 5)
board.put(1, 1)
board.put(2, 0)
board.printBoard()
board.rotate(True)
board.printBoard()
board.rotate(True)
board.printBoard()
board.rotate(False)
board.printBoard()
