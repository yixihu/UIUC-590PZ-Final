import pygame
import sys
import math
from RotatingConnect4.board import Board

blue = (32, 99, 155)
black = (23, 63, 95)
red = (237, 85 ,59)
yellow = (246, 213, 92)

squaresize = 96
radius = int(squaresize/2)
width = 6
height = 6
window_width = width * squaresize
window_height = height * squaresize

def updateBoard(board):
    for i in range(int(board.width)):
        for j in range(int(board.height)):
            pygame.draw.rect(screen, blue, (i * squaresize, j * squaresize + squaresize, squaresize, squaresize))
            pygame.draw.circle(screen, black, (
            int(i * squaresize + squaresize / 2), int(j * squaresize + squaresize + squaresize / 2)), int(radius))

    for i in range(board.width):
        for j in range(board.height):
            if board.board[j][i] == 1:
                pygame.draw.circle(screen, red,
                                    (int(i * squaresize + squaresize / 2), int(j * squaresize + squaresize / 2)),
                                    int(radius))
            elif board.board[j][i] == 2:
                pygame.draw.circle(screen, yellow,
                                    (int(i * squaresize + squaresize / 2), int(j * squaresize + squaresize / 2)),
                                    int(radius))
    pygame.display.update()
board = Board()

game_over = False
turn = 0
print(int(squaresize + squaresize / 2))
pygame.init()
size = (window_width, window_height)

screen = pygame.display.set_mode(size)
updateBoard(board)

pygame.display.update()
myfont = pygame.font.SysFont("monospace", 50)

while not game_over:
    pressed = pygame.key.get_pressed()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        if event.type == pygame.MOUSEMOTION:
            pygame.draw.rect(screen, black, (0, 0, window_width, squaresize))
            pos = event.pos[0]
            if pos <= squaresize:
                pos = int(squaresize / 2)
            elif pos > squaresize and pos <= squaresize * 2:
                pos = int(squaresize / 2 + squaresize)
            elif pos > squaresize * 2 and pos <= squaresize * 3:
                pos = int(squaresize / 2 + squaresize * 2)
            elif pos > squaresize * 3 and pos <= squaresize * 4:
                pos = int(squaresize / 2 + squaresize * 3)
            elif pos > squaresize * 4 and pos <= squaresize * 5:
                pos = int(squaresize / 2 + squaresize * 4)
            elif pos > squaresize * 5:
                pos = int(squaresize / 2 + squaresize * 5)

            if turn == 0:
                pygame.draw.circle(screen, red, (pos, int(squaresize / 2)), radius)
            else:
                pygame.draw.circle(screen, yellow, (pos, int(squaresize / 2)), radius)
        pygame.display.update()

        if event.type == pygame.MOUSEBUTTONDOWN:
            pygame.draw.rect(screen, black, (0, 0, window_width, squaresize))

            if turn == 0:
                pos = event.pos[0]
                col = int(math.floor(pos / squaresize))
                board.put(1, col)

                if board.checkOver():
                    label = myfont.render("Player 1 wins!!", 1, red)
                    screen.blit(label, (30, 10))
                    game_over = True


            else:
                pos = event.pos[0]
                col = int(math.floor(pos / squaresize))
                board.put(2, col)

                if board.checkOver():
                    label = myfont.render("Player 2 wins!!", 1, yellow)
                    screen.blit(label, (30, 10))
                    game_over = True

            board.printBoard()
            updateBoard(board)
            turn += 1
            turn = turn % 2

        if pressed[pygame.K_RIGHT]:
            board.rotate(True)
            if board.checkOver():
                if board.winningCoin == 1:
                    label = myfont.render("Player 1 wins!!", 1, red)
                else:
                    label = myfont.render("Player 2 wins!!", 1, yellow)
                screen.blit(label, (30, 10))
                game_over = True

            board.printBoard()
            updateBoard(board)
            turn += 1
            turn = turn % 2

        if pressed[pygame.K_LEFT]:
            board.rotate(False)
            if board.checkOver():
                if board.winningCoin == 1:
                    label = myfont.render("Player 1 wins!!", 1, red)
                else:
                    label = myfont.render("Player 2 wins!!", 1, yellow)
                screen.blit(label, (30, 10))
                game_over = True

            board.printBoard()
            updateBoard(board)
            turn += 1
            turn = turn % 2

pygame.time.wait(3000)
pygame.quit()