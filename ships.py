from dot import Dot


class Ship:
    def __init__(self, length, bow, orientation=0):
        self.length = length
        self.bow_point = bow
        self.orientation = orientation  # 1 vertical or 0 horizontal
        self.lives = length

    @property
    def dots(self):  # ship bow will be always at lower coords
        bow_points = []
        for i in range(self.length):
            bow_points.append(Dot(self.bow_point.coord_x + i * int(not self.orientation),
                                  self.bow_point.coord_y + i * self.orientation))
        return bow_points

    def ship_hit(self, shot):
        return shot in self.dots
