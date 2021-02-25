
class Unit:
    def __init__(self, unit_features: tuple):
        x, y, state, team, symbol = unit_features
        self.x = x
        self.y = y
        self.alive = state
        self.team = team
        self.symbol = symbol

