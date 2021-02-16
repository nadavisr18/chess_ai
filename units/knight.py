from units.unit import Unit


class Knight(Unit):
    def __init__(self, unit_features: tuple):
        super(Knight, self).__init__(unit_features)

    def move(self, x: int, y: int):
        if abs(self.x - x) > 2 or abs(self.y - y) > 2:
            return False
        elif abs(self.x - x) == 2 and abs(self.y - y) == 1:
            return True
        elif abs(self.y - y) == 2 and abs(self.x - x) == 1:
            return True
        else:
            return False
