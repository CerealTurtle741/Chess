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
    BOARD_SLOTS: dict[str, list[int | float]] = json.load(f)


# A dataclass to store the data for a square on a chess board
@dataclass
class Slot:
    rect: pygame.Rect
    square: str # e.g 'a1'
    piece: Piece | None = None


@dataclass
class Board:
    # screen to be passed in as the surface to be drawn to
    screen: pygame.surface.Surface

    # initialise the list for the slots
    # field(default_factory=list[Slot]) is the way to make an empty list in a dataclass
    slot_list: list[Slot] = field(default_factory=list[Slot])

    # values for moving pieces
    moving_piece: Piece | None = None
    starting_rect: pygame.rect.Rect | None = None

    # as a dataclass has an __init__ built in any methods to populate fields should be run in the __post_init__
    def __post_init__(self) -> None:
        self.make_rect()

    # makes th rects for the boards squares in the center of the screen
    def make_rect(self) -> None:
        for key, value in BOARD_SLOTS.items():
            x = value[0] + (self.screen.width - 8*60)/2
            y = value[1] + (self.screen.height - 8*60)/2
            width = value[2]
            height = value[3]
            self.slot_list.append(Slot(pygame.Rect(x, y, width, height), key))

    # adds a piece to a certain square
    # mainly for testing
    def add_piece(self, piece: Piece, pos: str) -> None:
        for slot in self.slot_list:
            if slot.square == pos:
                slot.piece = piece

    # gets the square hovered over by the mouse
    def get_slot(self) -> Slot | None:
        mouse = pygame.mouse.get_pos()
        for slot in self.slot_list:
            if slot.rect.collidepoint(mouse):
                return slot
        return None

    # moves a piece
    # first click selects the piece the second click places the piece
    # in future:
    #  - second click on own pieces selects that as the new piece
    #  - ability to capture pieces
    #  - only move if legal
    def move_piece(self, event: pygame.event.Event) -> None:
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            square = self.get_slot()
            if square is None:
                return
            if self.moving_piece is not None:
                if square.piece is not None:
                    return
                square.piece = self.moving_piece
                self.moving_piece = None
                return
            if square.piece is None:
                return
            self.moving_piece = square.piece
            self.starting_rect = square.rect
            square.piece = None

    # method to capture all methods that require events from the main game loop e.g clicking buttons
    def player_input(self, event: pygame.event.Event) -> None:
        self.move_piece(event)

    # draws the pieces and squares in a chess board
    def draw(self) -> None:
        for i, slot in enumerate(self.slot_list):
            i += i//8
            if (i+1) % 2:
                pygame.draw.rect(self.screen, (0,0,0), slot.rect)
            else:
                pygame.draw.rect(self.screen, (255,255,255), slot.rect)
            if slot.piece is not None and slot.piece.image is not None:
                self.screen.blit(slot.piece.image, slot.rect)
        if self.moving_piece is not None and self.moving_piece.image is not None and self.starting_rect is not None:
            self.screen.blit(self.moving_piece.image, self.starting_rect)