from math import *
from typing import Self,Type

class Point2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distance_to_origin(self) -> float:
        return sqrt(self.x**2 + self.y**2)

    def distance_to_other(self, other: Type[Self]) -> float:
        return sqrt((self.x - other.x)** + (self.y - other.y)**2)