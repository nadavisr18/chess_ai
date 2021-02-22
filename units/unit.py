from board.board import Board


class Unit:
    def __init__(self, unit_features: tuple):
        x, y, state, team, symbol = unit_features
        self.x = x
        self.y = y
        self.alive = state
        self.team = team
        self.symbol = symbol


    def allowed_moves(self, move_func):
        pass

    def move_unit(self, board: Board, target_x: int, target_y: int):
        board.board_list[self.y][self.x] = None
        self.x = target_x
        self.y = target_y
        if board.board_list[target_y][target_x] is not None:
            board.handel_dead_units(board.board_list[target_y][target_y])
        board.board_list[target_y][target_x] = self
