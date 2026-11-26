import pygame
from sys import exit
from pieces import Piece
from board import Board

# chess pieces from https://commons.wikimedia.org/wiki/File:ChessPiecesArray.png
SHEET = 'ChessPiecesArray.png'
BLACK = (255, 255, 255)
WIDTH = 800
HEIGHT = 800

pygame.init()
SCREEN: pygame.Surface = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Chess')

white_pawn = Piece(SHEET, 'rook', 'white')
square = 'a1'
board = Board(SCREEN)
board.add_piece(white_pawn, square)


def main():
    # Set up game loop
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running =False
        SCREEN.fill((150, 0, 100))
        board.draw()
        pygame.display.update()
    pygame.quit()
    exit()

if __name__ == '__main__':
    main()
