from math import sqrt


class Point:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def calculate_distance(self, point_b):
        return sqrt((self.x - point_b.x) ** 2 + (self.y - point_b.y) ** 2 + (self.z - point_b.z) ** 2)
