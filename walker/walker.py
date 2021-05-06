#!/usr/bin/env python3

from math import floor
from random import randrange

from noise import PerlinNoise


class Walker:
    """A class to generate random walks in a two dimentional grid."""

    def __init__(self, x, y, grid, size):
        """Initiate a new walker for a square grid of <size> dimensions.

        Preconditions:
            - <x> and <y> are integers greater than zero and less than <size>.
            - <grid> is a two dimentional square numpy array.
            - <size> is the dimensions of <grid>.
        """
        self.x = x
        self.y = y

        # TODO: Consider adding random starting offsets.
        # Fix these names.
        self.xx_off = 0
        self.xy_off = 10000
        self.yx_off = 5000
        self.yy_off = 15000

        self.grid = grid
        self.size = size

        # Get our noise generator
        self.noise = PerlinNoise(original_perm=False)

    # TODO: Add check for grid boundaries. Either stop movement, or roll over.
    def step(self, frame_number, image):
        """Move this Walker by a single movement by adding a randomly selected
        value from -1, 0, or 1 to the current x and y values of the current
        position.
        
        A move is represented by setting the value of self.grid at the new x and
        y values to 255.

        <image> is then sent to contain the newly updated grid for display
        purposes.

        Precondition:
            - <image> is an AxesImage from the matplotlib library.
        """
        # Get random values to step by.
        step_x = randrange(3) - 1
        step_y = randrange(3) - 1

        # Check if in bounds and update.
        if abs(self.x + step_x) < self.size:
            self.x += step_x
        if abs(self.y + step_y) < self.size:
            self.y += step_y

        # Update grid.
        self.grid[self.x, self.y] = 255

        # Update image with newly updated grid.
        image.set_data(self.grid)

        return image,

    def note_step(self, frame_number, image):
        """This is just to record an idea based on Monte Carlo, don't actually
        call this.

        This gets stuck close to (0, 0), maybe adjust this somehow?
        """
        # Select random step size.
        step_size = randrange(1, 10)

        # Get random values to step by.
        step_x = randrange(-step_size, step_size)
        step_y = randrange(-step_size, step_size)

        # This will take a custom step checking function maybe.
        # Start with just writing the normal one.
        if abs(self.x + step_x) <= self.size:
            self.x += step_x
        if abs(self.y + step_y) <= self.size:
            self.y += step_y

        # Update grid.
        self.grid[self.x, self.y] = 255

        # Update image with newly updated grid.
        image.set_data(self.grid)

        return image,

    def _map(self, x, a, b, c, d):
        """Map the value <x> in the interval <a> to <b> to its corresponding
        value in the interval <c> to <d>. This is using the linear transform
                                (x - a)(d - c)
                                -------------- + c
                                    (b - a)
        """
        return c + (x - a) / (b - a) * (d - c)

    def noise_step(self, frame_number, image):
        """Move this Walker by a single movement by generating values from an
        implementation of two dimensional Perlin Noise based on offsets for
        x and y, and map the returned value to a position in the grid.
        
        A move is represented by setting the value of self.grid at the new x and
        y values to 255.

        <image> is then sent to contain the newly updated grid for display
        purposes.

        Precondition:
            - <image> is an AxesImage from the matplotlib library.
        """
        # Get random values for new position.
        self.x = floor(self._map(self.noise.generate(self.xx_off, self.xy_off),
                                 -0.707106, 0.707106, 0, self.size - 1))
        self.y = floor(self._map(self.noise.generate(self.yx_off, self.yy_off),
                                 -0.707106, 0.707106, 0, self.size - 1))

        # TODO: Fix these names.
        # Increment offsets.
        self.xx_off += 0.01
        self.xy_off += 0.01
        self.yx_off += 0.01
        self.yy_off += 0.01

        # Prevent self.x and self.y from being out of bounds.
        if self.x >= 100:
            self.x = 99
        if self.y >= 100:
            self.y = 99

        # Update grid.
        self.grid[self.x, self.y] = 255

        # Update image with newly updated grid.
        image.set_data(self.grid)

        return image,
