#!/usr/bin/env Python3

""""""

from random import randrange

from .vector import Vector


class Mover:
    """"""

    def __init__(self, grid, size, location, velocity, acceleration):
        """"""
        # Grid and grid information.
        self.grid = grid
        self.size = size

        # Vectors.
        self.location = location
        self.velocity = velocity
        self.acceleration = acceleration

    def _update(self):
        """"""
        # Create random direction of acceleration.
        self.acceleration = Vector(randrange(-1, 1), randrange(-1, 1))
        # Scale acceleration by a random amount.
        

        # Add to velocity and limit speed.
        self.velocity.add(self.acceleration)
        self.velocity.limit(10)

        self.location.add(self.velocity)

    def _check_edges(self):
        """"""
        if self.location.x >= self.size:
            self.location.x = 0
        elif self.location.x < 0:
            self.location.x = self.size - 1

        if self.location.y >= self.size:
            self.location.y = 0
        elif self.location.y < 0:
            self.location.y = self.size - 1

    def move(self, frame_number, image):
        """"""
        # Set initial location to black.
        self.grid[round(self.location.x), round(self.location.y)] = 0

        self._update()
        self._check_edges()

        # Prevent self.x and self.y from being out of bounds.
        if round(self.location.x) >= 100:
            self.location.x = 99
        if round(self.location.y) >= 100:
            self.location.y = 99

        # Update grid.
        self.grid[round(self.location.x), round(self.location.y)] = 255

        # Update image with newly updated grid.
        image.set_data(self.grid)

        return image,

    # TODO: Fix wrapping and make the bounce more bounce like.
    def _check_edges_bounce(self):
        """"""
        if self.location.x >= self.size - 1 or self.location.x <= 1:
            self.velocity.x *= -1
            self.acceleration.x *= -1

        if self.location.y >= self.size - 1 or self.location.y <= 1:
            self.velocity.y *= -1
            self.acceleration.y *= -1

    def bounce(self, frame_number, image):
        """"""
        # Set initial location to black.
        self.grid[round(self.location.x), round(self.location.y)] = 0

        self._update()
        self._check_edges_bounce()

        # Prevent self.x and self.y from being out of bounds.
        if round(self.location.x) >= 100:
            self.location.x = 99
        if round(self.location.y) >= 100:
            self.location.y = 99

        # Update grid.
        self.grid[round(self.location.x), round(self.location.y)] = 255

        # Update image with newly updated grid.
        image.set_data(self.grid)

        return image,
