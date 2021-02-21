
import re
from units.bishop import *
from units.king import *
from units.knight import *
from units.pawn import *
from units.queen import *
from units.rook import *

# board_row_size and board_column_size needs to be imported from config

class Board:
    def __init__(self):
        self.board_list = []
        for i in range(board_column_size):
            l = []
            for i in range(board_row_size):
                l.append(None)

            self.board_list.append(l)

    def display(self):
        for i in self.board_list:
            for unit in i:
                if unit is None:
                    print("Empty", end=" ")
                else:
                    print(unit.symbol, end=" ")
            print("\n")

    def fen_to_board(self, fen: str):
        current_y = 0
        current_x = 0
        for char in fen:
            if re.search(r"\d", char):
                current_x += int(char)

            elif char == "/":
                current_x = 0
                current_y += 1

            else:
                self.board_list[current_y][current_x] = self.get_unit(char, current_x, current_y)
                current_x += 1

    # Fix Pawn to not always be "not moved"
    @staticmethod
    def get_unit(char: str, x: int, y: int):
        if char == "P":
            return Pawn((x, y, True, "w", char), True)

        elif char == "p":
            return Pawn((x, y, True, "b", char), True)

        elif char == "R":
            return Rook((x, y, True, "w", char))

        elif char == "r":
            return Rook((x, y, True, "b", char))

        elif char == "N":
            return Knight((x, y, True, "w", char))

        elif char == "n":
            return Knight((x, y, True, "b", char))

        elif char == "B":
            return Bishop((x, y, True, "w", char))

        elif char == "b":
            return Bishop((x, y, True, "b", char))

        elif char == "Q":
            return Queen((x, y, True, "w", char))

        elif char == "q":
            return Queen((x, y, True, "b", char))

        elif char == "K":
            return King((x, y, True, "w", char))

        elif char == "k":
            return King((x, y, True, "b", char))


b = Board()

fen = "rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR"

b.fen_to_board(fen)
b.display()