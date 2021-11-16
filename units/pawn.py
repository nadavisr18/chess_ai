from units.unit import Unit

# Maybe want to hard code that pawn always is created with is moved from start = false

class Pawn(Unit):
    def __init__(self, unit_features: tuple):
        super(Pawn, self).__init__(unit_features)
        if self.team == "b" and self.y == 1:
            self.moved_from_start = False
        elif self.team == "w" and self.y == 6:
            self.moved_from_start = False
        else:
            self.moved_from_start = True

    def move(self, x: int, y: int, board):
        if self.x != x and abs(self.x - x) == 1:
            from board.board import Board
            if (self.y-y) == 1 and self.team =="w":
                if board.board_list[y][x] is not None and board.board_list[y][x].team != self.team:
                    return True
                else:
                    return False
            elif (self.y-y) == -1 and self.team =="b":
                if board.board_list[y][x] is not None and board.board_list[y][x].team != self.team:
                    return True
                else:
                    return False
            else:
                return False
        elif self.x != x:
            return False
        else:
            if abs(self.y - y) > 1:
                if self.moved_from_start:
                    return False
                else:
                    if abs(self.y - y) == 2:
                        if self.team == "b":
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
                if self.team == "b":
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
