from pathlib import Path
import json
import pygame
from dataclasses import dataclass, field
from pieces import Piece


# Finding the path of the file so it works on all machines
base_dir = Path(__file__).resolve().parent
folder_dir = base_dir / 'board_data'
file_dir = folder_dir / 'slots.json'
# Loads the slot data in the form 'square (e.g a1)': [slot rect]
with open(file_dir) as f:
    BOARD_SLOTS: dict[str, list[int]] = json.load(f)


@dataclass
class Slot:
    rect: pygame.Rect
    square: str
    piece: Piece | None = None


@dataclass
class Board:
    screen: pygame.surface.Surface
    slot_list: list[Slot] = field(default_factory=list[Slot])
    def __post_init__(self) -> None:
        for key, value in BOARD_SLOTS.items():
            self.slot_list.append(Slot(pygame.Rect(value), key))

    def add_piece(self, piece: Piece, pos: str) -> None:
        for slot in self.slot_list:
            if slot.square == pos:
                slot.piece = piece

    def player_input(self, event: pygame.event.Event) -> None:
        raise NotImplementedError

    def update(self) -> None:
        raise NotImplementedError

    def draw(self) -> None:
        for slot in self.slot_list:
            if slot.piece is not None and slot.piece.image is not None:
                self.screen.blit(slot.piece.image, slot.rect)