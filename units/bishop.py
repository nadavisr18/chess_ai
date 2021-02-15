from units.unit import Unit


class Bishop(Unit):
    def __init__(self, unit_features: tuple):
        super(Bishop, self).__init__(unit_features)

    def move(self, x: int, y: int):
        if x == self.x or y == self.y:
            return False
        elif abs(x - self.x) == abs(y - self.y):
            return True
        else:
            return False
