class Dot:
    def __init__(self, x, y):
        self.coord_x = x
        self.coord_y = y

    def __eq__(self, o):
        return self.coord_x == o.coord_x and self.coord_y == o.coord_y

    def __repr__(self):
        return f"Dot({self.coord_x}, {self.coord_y})"