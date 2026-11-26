"""
Create a json file with all the slot rects relative to the board
The pieces are 60x60 pixels
As pygame reads the origin as the top left corner the slots 
are arranged so that they originate from the top left too
"""
import json
import chess
from pathlib import Path
from settings import PIECE_SIZE

base_dir = Path(__file__).resolve().parent
file_dir = base_dir / 'slots.json'


data = {}
for i in range(64):
    square_name: str = chess.square_name(i)
    file = chess.square_file(i)
    rank = chess.square_rank(i)
    data[square_name] = [file*PIECE_SIZE,
                         (7-rank)*PIECE_SIZE,
                         PIECE_SIZE,
                         PIECE_SIZE
                         ]

with open(file_dir, 'w', encoding='utf-8') as f:
    json.dump(data, f, indent=4)