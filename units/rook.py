from units.unit import Unit


class Rook(Unit):
    def __init__(self, unit_features: tuple):
        super(Rook, self).__init__(unit_features)
        if self.team == "b" and self.y == 0 and self.x in [0, 7]:
            self.moved_from_start = False
        elif self.team == "w" and self.y == 6 and self.x in [0, 7]:
            self.moved_from_start = False
        else:
            self.moved_from_start = True

    def move(self, x: int, y: int):
        if self.x == x and self.y == y:
            return False
        elif self.x == x or self.y == y:
            return True
        else:
            return False
