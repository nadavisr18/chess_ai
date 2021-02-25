from units.unit import Unit


class King(Unit):
    def __init__(self, unit_features: tuple):
        super(King, self).__init__(unit_features)
        if self.team == "b" and self.x == 4 and self.y == 0:
            self.moved_from_start = False
        elif self.team == "w" and self.x == 4 and self.y == 7:
            self.moved_from_start = False
        else:
            self.moved_from_start = True

    def move(self, x: int, y: int):
        if abs(self.x - x) > 1 or abs(self.y - y) > 1:
            return False
        else:
            return True
