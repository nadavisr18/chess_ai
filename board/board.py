
import re
from units.unit import Unit
from units.bishop import Bishop
from units.king import King
from units.knight import Knight
from units.pawn import Pawn
from units.queen import Queen
from units.rook import Rook

# board_row_size and board_column_size needs to be imported from config

board_column_size = 8
board_row_size = 8

class Board:
    def __init__(self):
        self.dead_w = []
        self.dead_b = []
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
                    print("*", end="  ")
                else:
                    print(unit.symbol, end="  ")
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

    def allowed_moves(self, unit: Unit):
        moves_list = []
        for y in range(board_column_size):
            temp_list = []
            for x in range(board_row_size):
                if unit is not None:
                    if unit.symbol in ["p", "P"]:
                        temp_list.append(unit.move(x, y, self))
                    else:
                        temp_list.append(unit.move(x, y))
            moves_list.append(temp_list)
        moves_list = unit.collision_detection(moves_list, self.board_list)
        for x in range(len(moves_list)):
            print(moves_list[x])
        return moves_list

    def move_unit(self, unit: Unit, target_x: int, target_y: int):
        self.board_list[unit.y][unit.x] = None
        unit.x = target_x
        unit.y = target_y
        if self.board_list[target_y][target_x] is not None:
            self.handel_dead_units(self.board_list[target_y][target_y])
        self.board_list[target_y][target_x] = unit

    def handel_dead_units(self, unit: Unit):
        if unit.team == "w":
            self.dead_w.append(unit)
        elif unit.team == "b":
            self.dead_b.append(unit)
        self.board_list[unit.y].remove(unit)
        unit.alive = False

    # Fix Pawn to not always be "not moved"
    @staticmethod
    def get_unit(char: str, x: int, y: int):
        if char == "P":
            return Pawn((x, y, True, "w", char))

        elif char == "p":
            return Pawn((x, y, True, "b", char))

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


