

class Unit:
    def __init__(self, unit_features: tuple):
        x, y, state, team = unit_features
        self.x = x
        self.y = y
        self.alive = state
        self.team = team

    def allowed_moves(self, move_func):
        allowed_moves = []
        for cell in board:
            allowed_moves.append(move_func(cell))




