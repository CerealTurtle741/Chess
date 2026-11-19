import pygame
from spritesheet import Spritesheet


piece_index = ['queen', 'king', 'rook', 'knight', 'bishop', 'pawn']


class Piece(pygame.sprite.Sprite):
    def __init__(
            self,
            spritesheet: str,
            piece: str,
            color: str
            ) -> None:

        self.spritesheet_image = pygame.image.load(spritesheet).convert_alpha()
        self.piece_name = piece
        self.color = color
        self.sheet_index: list[int] = [0, 0]

        for i, pieces in enumerate(piece_index):
            if pieces == self.piece_name:
                self.sheet_index[0] = i
            else:
                raise PieceNameException(f'Piece: {self.piece_name} is not a valid piece')

        if self.color == 'black':
            self.sheet_index[1] = 0
        elif self.color == 'white':
            self.sheet_index[1] = 1
        else:
            raise PieceColorException(f'Color: {self.color} is not valid for the game\nAccepted Colors: ["black", "white"]')

        self.image = Spritesheet(self.spritesheet_image).get_image(60, 60, self.sheet_index[0], self.sheet_index[1], 3)
        self.rect = self.image.get_rect()


class PieceException(Exception):
    """An exception for pieces"""
class PieceNameException(PieceException):
    """If the piece's name is not in the index for the pieces"""
class PieceColorException(PieceException):
    """If the piece's color is not right"""

