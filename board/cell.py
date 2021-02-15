from units.unit import Unit


class Cell:
    def __init__(self, x_cord: int, y_cord: int, occupied: bool, current_unit: Unit):
        self.x_cord = x_cord
        self.y_cord = y_cord
        self.occupied = occupied
        self.current_unit = current_unit
