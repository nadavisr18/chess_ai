from units.unit import Unit


class Rook(Unit):
    def __init__(self, unit_features: tuple, moved_from_start: bool):
        super(Rook, self).__init__(unit_features)
        self.moved_from_start = moved_from_start

    def move(self, x: int, y: int):
        if self.x == x and self.y == y:
            return False
        elif self.x == x or self.y == y:
            return True
        else:
            return False
