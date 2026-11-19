import pygame
from spritesheet import Spritesheet
piece_index = ['queen', 'king', 'rook', 'knight', 'bishop', 'pawn']
class Piece:
  def __init__(
    self,
    piece: str,
    color: str
  ) -> None:
    self.piece_name = piece
    self.color = color
    self.sheet_index = [None, None]
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
      raise PieceColorException(f'Color: {self.color} is not valid for the game\nColors = ["black", "white"]')

    def get_image(
      self,
      spritesheet: str,
      width: int,
      height: int,
      scale: int
    ) -> pygame.Surface:
      image = Spritesheet(spritesheet).get_image(width, height, *self.sheet_index, scale, color)
      return image
      
class PieceException(Exception):
  """An exception for pieces"""
class PieceNameException(PieceException):
  """If the piece's name is not in the index for the pieces"""
class PieceColorException(PieceException):
  """If the piece's color is not right"""
  
