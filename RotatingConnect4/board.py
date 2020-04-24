import math
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

    def copy(self):
        newBoard = Board()
        copyBoard = []
        for i in range(self.height):
            temp = []
            for j in range(self.width):
                temp.append(self.board[i][j])
            copyBoard.append(temp)

        newBoard.board = copyBoard
        newBoard.gameOver =self.gameOver
        newBoard.winningCoin = self.winningCoin
        return newBoard

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
                    if self.board[i][j] == self.board[i][j + 1] == self.board[i][j + 2] == self.board[i][j + 3] != 0:
                        self.winningCoin = self.board[i][j]
                        self.gameOver = True
                except IndexError:
                    pass

                try:
                    if self.board[i][j] == self.board[i + 1][j] == self.board[i + 2][j] == self.board[i + 3][j] != 0:
                        self.winningCoin = self.board[i][j]
                        self.gameOver = True
                except IndexError:
                    pass

                try:
                    if self.board[i][j] == self.board[i + 1][j + 1] == self.board[i + 2][j + 2] == self.board[i + 3][j + 3] != 0:
                        self.winningCoin = self.board[i][j]
                        self.gameOver = True
                except IndexError:
                    pass

                try:
                    if self.board[i][j] == self.board[i - 1][j + 1] == self.board[i - 2][j + 2] == self.board[i - 3][j + 3] != 0:
                        self.winningCoin = self.board[i][j]
                        self.gameOver = True
                except IndexError:
                    pass
        return self.gameOver

    def validCol(self):
        columns = []
        for i in range(self.width):
            if self.board[0][i] == 0:
                columns.append(i)
        return columns

    def validMove(self):
        moves = [['r', True], ['r', False]]
        for i in range(self.width):
            if self.board[0][i] == 0:
                moves.append(['d', i])
        return moves

    def printBoard(self):
        # print out the board
        for i in range(self.height):
            print("-" * (4 * (self.width) + 1))
            for j in range(self.width):
                print("| " + str(self.board[i][j]), end=" ")
                if j == self.width - 1:
                    print("|")
        print("-" * (4 * (self.width) + 1))


# test = [[0,0,0,0,0,0],
#         [0,0,0,0,0,0],
#         [0,0,0,0,0,1],
#         [0,0,0,2,1,2],
#         [0,0,2,1,2,1],
#         [0,0,1,2,1,2]]
#
# board = Board()
# board.put(1, 2)
# board.put(2, 2)
# board.put(1, 1)
# board.put(2, 3)
# board.put(1, 1)
# board.put(2, 1)
# board.put(1, 3)
# board.put(2, 5)
# board.put(1, 1)
# board.put(2, 0)
# board.printBoard()
# board.rotate(True)
# board.printBoard()
# board.rotate(True)
# board.printBoard()
# board.rotate(False)
# board.printBoard()
#
# board.setBoard(test)
# board.printBoard()
# print(board.checkOver())