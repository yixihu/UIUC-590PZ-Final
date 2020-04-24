from RotatingConnect4.board import Board
import math
import random


def heuristic(board, coin: 1):
    value = 0
    for i in range(board.height):
        for j in range(board.width):
            try:
                # horizontally check connected coins
                if board.board[i][j] == board.board[i][j + 1] == coin:
                    value += 1
                if board.board[i][j] == board.board[i][j + 1] == board.board[i][j + 2] == coin:
                    value += 50
                if board.board[i][j] == board.board[i][j + 1] == board.board[i][j + 2] == board.board[i][j + 3] == coin:
                    value += 10000000
            except IndexError:
                pass

            try:
                # vertically check connected coins
                if board.board[i][j] == board.board[i + 1][j] == coin:
                    value += 1
                if board.board[i][j] == board.board[i + 1][j] == board.board[i + 2][j] == coin:
                    value += 50
                if board.board[i][j] == board.board[i + 1][j] == board.board[i + 2][j] == board.board[i + 3][j] == coin:
                    value += 10000000
            except IndexError:
                pass

            # diagonally check connected coins
            try:
                if board.board[i][j] == board.board[i + 1][j + 1] == coin:
                    value += 1
                if board.board[i][j] == board.board[i + 1][j + 1] == board.board[i + 2][j + 2] == coin:
                    value += 50
                if board.board[i][j] == board.board[i + 1][j + 1] == board.board[i + 2][j + 2] == board.board[i + 3][j + 3] == coin:
                    value += 10000000
            except IndexError:
                pass

            try:
                if board.board[i][j] == board.board[i + 1][j - 1] == coin:
                    value += 1
                if board.board[i][j] == board.board[i + 1][j - 1] == board.board[i + 2][j - 2] == coin:
                    value += 50
                if board.board[i][j] == board.board[i + 1][j - 1] == board.board[i + 2][j - 2] == board.board[i + 3][j - 3] == coin:
                    value += 10000000
            except IndexError:
                pass

    return value


def miniMax(board, depth, maxPlayer, alpha, beta):
    if maxPlayer:
        coin = 2
    else:
        coin = 1
    board.checkOver()
    if board.gameOver:
        return (heuristic(board, coin), None)
    elif depth == 0:
        return (heuristic(board, coin), None)
    else:
        ##
        validMoves = board.validMove()
        # validColumns = board.validCol()
        if maxPlayer:
            maxValue = -math.inf
            ##
            move = random.choice(validMoves)
            # column = random.choice(validColumns)

            for movePair in validMoves:
                newBoard = board.copy()
                if movePair[0] == 'r':
                    # rotate
                    newBoard.rotate(movePair[1])
                elif movePair[0] == 'd':
                    # dropping
                    newBoard.put(coin, movePair[1])

                # newBoard.put(coin, col)
                outCome = miniMax(newBoard, depth - 1, False, alpha, beta)[0]
                if outCome > maxValue:
                    maxValue = outCome
                    move = movePair
                alpha = max(maxValue, alpha)
                if alpha >= beta:
                    break
            return (maxValue, move)
        else:
            minValue = math.inf
            move = random.choice(validMoves)
            # column = random.choice(validColumns)

            for movePair in validMoves:
                newBoard = board.copy()
                if movePair[0] == 'r':
                    # rotate
                    newBoard.rotate(movePair[1])
                elif movePair[0] == 'd':
                    # dropping
                    newBoard.put(coin, movePair[1])

                outcome = miniMax(newBoard, depth - 1, True, alpha, beta)[0]
                if outcome < minValue:
                    minValue = outcome
                    move = movePair
                beta = min(minValue, beta)
                if alpha >= beta:
                    break
            return (minValue, move)



if __name__ == '__main__':
    # generate the empty board for game
    newGame = Board()

    # player vs AI game
    # decide which one goes first, True for player goes first, otherwise AI goes first
    firstHand = [True, False]
    goFirst = random.choice(firstHand)
    print("=============== Game Start ===============")

    while not newGame.gameOver:
        if goFirst:

            moves = newGame.validCol()
            move = random.choice(moves)
            newGame.put(1, move)
            newGame.checkOver()
            newGame.printBoard()
            goFirst = not goFirst
        else:
            move = miniMax(newGame, 6, True, -math.inf, math.inf)[1]
            if move[0] == 'r':
                newGame.rotate(move[1])
                #print("Rotating!!!!!!!!!!!!!")
            elif move[0] == 'd':
                newGame.put(2, move[1])

            newGame.checkOver()
            newGame.printBoard()
            goFirst = not goFirst

    print("=============== Game Over ===============")
    print("Player " + str(newGame.winningCoin) + " wins!!!!!!!!!!")