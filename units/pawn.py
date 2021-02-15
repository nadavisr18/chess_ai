from units.unit import Unit


class Pawn(Unit):
    def __init__(self, unit_features: tuple):
        super(Pawn, self).__init__(unit_features)