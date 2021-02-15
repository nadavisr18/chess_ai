from cell import *

class Board:
    def __init__(self):
        self.board = []
        for i in range(8):
            l = []
            for i in range(8):
                l.append(Cell(None))

            self.board.append(l)