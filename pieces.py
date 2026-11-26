import pygame
from spritesheet import Spritesheet
import settings




def get_piece(color: str, piece_name: str) -> tuple[int, int]:
    piece_index: int | None = None
    color_index: int | None = None
    for i, piece in enumerate(settings.PIECES):
        if piece == piece_name:
            piece_index = i
    if piece_index is None:
        raise PieceNameException(f'Piece: {piece_name} is not a valid piece')
    if color == 'white':
        color_index = 1
    elif color == 'black':
        color_index = 0
    else:
        raise PieceColorException(f'Color: {color} is not valid for the game\nAccepted Colors: ["black", "white"]')
    print(piece_index, color_index)
    return (piece_index, color_index)


class Piece(pygame.sprite.Sprite):
    def __init__(
            self,
            spritesheet: str,
            piece: str,
            color: str
            ) -> None:
        super().__init__()
        self.spritesheet_image = pygame.image.load(spritesheet).convert_alpha()
        self.piece_name = piece
        self.color = color
        self.sheet_index: tuple[int, int] = get_piece(color, piece)
        self.image = Spritesheet(self.spritesheet_image).get_image(60, 60, *self.sheet_index, 1)
        self.rect = self.image.get_rect()


class PieceException(Exception):
    """An exception for pieces"""
class PieceNameException(PieceException):
    """If the piece's name is not in the index for the pieces"""
class PieceColorException(PieceException):
    """If the piece's color is not right"""

