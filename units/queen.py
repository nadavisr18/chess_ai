from units.unit import Unit


class Queen(Unit):
    def __init__(self, unit_features: tuple):
        super(Queen, self).__init__(unit_features)

    def move(self, x: int, y: int):
        if self.x == x or self.y == y:
            return False
        elif self.x == x or self.y == y:
            return True
        elif abs(x - self.x) == abs(y - self.y):
            return True
        else:
            return False
