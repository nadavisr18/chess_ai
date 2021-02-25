from units.unit import Unit


class King(Unit):
    def __init__(self, unit_features: tuple, moved_from_start: bool):
        super(King, self).__init__(unit_features)
        self.moved_from_start = moved_from_start

    def move(self, x: int, y: int):
        if abs(self.x - x) > 1 or abs(self.y - y) > 1:
            return False
        else:
            return True
