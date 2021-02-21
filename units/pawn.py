from units.unit import Unit

# Maybe want to hard code that pawn always is created with is moved from start = false

class Pawn(Unit):
    def __init__(self, unit_features: tuple, moved_from_start: bool):
        super(Pawn, self).__init__(unit_features)
        self.moved_from_start = moved_from_start

    def move(self, x: int, y: int):
        if self.x != x and abs(self.x - x) == 1:
            if board.board_list[y[x]].team != self.team:
                return True
            else:
                return False
        else:
            if abs(self.y - y) > 1:
                if self.moved_from_start:
                    return False
                else:
                    if abs(self.y - y) == 2:
                        if self.team == "black":
                            if y < self.y:
                                return False
                            else:
                                return True
                        else:
                            if y > self.y:
                                return False
                            else:
                                return True
                    else:
                        return False

            elif abs(self.y - y) == 1:
                if self.team == "black":
                    if y < self.y:
                        return False
                    else:
                        return True
                else:
                    if y > self.y:
                        return False
                    else:
                        return True
            else:
                return False
