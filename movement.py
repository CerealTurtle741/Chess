from spritesheet import Spritesheet #Importing the function that creates a sprite sheet then defines the image used and its parameters 
from python_chess_instal import Board, Move, Outcome, Termination #Importing the chess library that will be used to create the chess board and pieces
from pieces import Piece #Importing the class that will be used to create the chess pieces
import chess
import pygame
board= chess.Board()  
class side(Piece):
     n=1
     while board.is_checkmate() == False and n<10:
      turn = n 
      if turn % 2 == 0:
          
      if turn % 2 == 1:
         
      n=n+1
      print(turn)
