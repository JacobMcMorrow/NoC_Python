#!/usr/bin/env Python3

""""""

from dataclasses import dataclass
from math import sqrt


# TODO: Figure out how to make this model multiple vector dimensions.
@dataclass
class Vector:
    """"""
    x: float
    y: float

    def add(self, other):
        """"""
        self.x += other.x
        self.y += other.y

    def sub(self, other):
        """"""
        self.x -= other.x
        self.y -= other.y

    def mul(self, other):
        """"""
        self.x *= other
        self.y *= other

    def div(self, other):
        """"""
        self.x /= other
        self.y /= other

    def mag(self):
        """"""
        return sqrt(self.x * self.x + self.y * self.y)

    def set_mag(self, magnitude):
        """"""
        if magnitude == 0:
            self.x = 0
            self.y = 0
        elif self.mag() != magnitude:
            self.normalize()
            self.mult(magnitude)

    def normalize(self):
        """"""
        magnitude = self.mag()

        if magnitude != 0:
            self.div(magnitude)

    def limit(self, maximum):
        """"""
        if self.mag() > maximum:
            self.normalize()
            self.mul(maximum)

    def heading(self, other):
        """"""
        pass

    def rotate(self, other):
        """"""
        pass

    def lerp(self, other):
        """"""
        pass

    def dist(self, other):
        """"""
        pass

    def angle_between(self, other):
        """"""
        pass

    def dot(self, other):
        """"""
        return self.x * other.x + self.y * other.y
    
    '''
    Only matters for three dimensional vectors.
    def cross(self, other):
        """"""
        pass
    '''
