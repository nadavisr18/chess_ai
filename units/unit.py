
class Unit:
    def __init__(self, unit_features: tuple):
        x, y, state, team = unit_features
        self.x = x
        self.y = y
        self.alive = state
        self.team = team

    def allowed_moves(self, move_func):
        for cell in board:
            if move_func(cell.x_cord, cell.y_cord):
                if cell.occupied:
                    occupied_cell_cords = (cell.x_cord, cell.y_cord)
                    if cell.current_unit.team == self.team:
                        # not allowed
                    else:
                        # allowed

                else:
                    # allowed
