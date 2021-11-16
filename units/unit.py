
class Unit:
    def __init__(self, unit_features: tuple):
        x, y, state, team, symbol = unit_features
        self.x = x
        self.y = y
        self.alive = state
        self.team = team
        self.symbol = symbol

    def relative_pos(self, target_Unit):
        if self.x == target_Unit.x and self.y > target_Unit.y:
            return "y<"

        elif self.x == target_Unit.x and self.y < target_Unit.y:
            return "y>"

        elif self.x > target_Unit.x and self.y == target_Unit.y:
            return "x<"

        elif self.x < target_Unit.x and self.y == target_Unit.y:
            return "x>"

        elif self.x < target_Unit.x and self.y < target_Unit.y:
            return "x>y>"

        elif self.x > target_Unit.x and self.y > target_Unit.y:
            return "x<y<"

        elif self.x < target_Unit.x and self.y > target_Unit.y:
            return "x>y<"

        elif self.x > target_Unit.x and self.y < target_Unit.y:
            return "x<y>"

    def collision_detection(self, moves_list: list, board_list: list):
        blocking_units = []
        for y in range(len(moves_list)):
            for x in range(len(moves_list[y])):
                if moves_list[y][x] and board_list[y][x] is not None:
                    blocking_unit = board_list[y][x]
                    rel_pos = self.relative_pos(blocking_unit)

                    # Vertical Up
                    if rel_pos == "y<":
                        for z in moves_list:
                            if moves_list.index(z) <= blocking_unit.y:
                                moves_list[moves_list.index(z)][self.x] = False
                        if self.team != blocking_unit.team and self.symbol not in ["p","P"]:
                            moves_list[blocking_unit.y][blocking_unit.x] = True

                    # Vertical Down
                    if rel_pos == "y>":
                        largest_y_blocking_unit = 0
                        for z in moves_list:
                            if moves_list.index(z) >= blocking_unit.y:
                                moves_list[moves_list.index(z)][self.x] = False
                        if self.team != blocking_unit.team and self.symbol not in ["p", "P"]:
                            moves_list[blocking_unit.y][blocking_unit.x] = True


        return moves_list
