from cell import *

# board_row_size and board_column_size needs to be imported from config

class Board:
    def __init__(self):
        self.board = []
        for i in range(board_row_size):
            l = []
            for i in range(board_column_size):
                l.append(Cell(None))

            self.board.append(l)