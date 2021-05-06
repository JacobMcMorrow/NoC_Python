#!/usr/bin/env python3

""""""

import argparse

import numpy as np

from display import Display
from user_input import UserInput
from vector.vector import Vector
from vector.motion import Mover
from walker.walker import Walker


def main():
    """"""
    user_input = UserInput()
    arguments = user_input.get_arguments()

    # Keep this for when you're working with a random grid.
    # grid = np.random.choice([255, 0],
    #                         arguments["grid_size"] * arguments["grid_size"],
    #                         p = [0.2, 0.8]).reshape(arguments["grid_size"],
    #                                                 arguments["grid_size"])

    grid = np.zeros((arguments["grid_size"], arguments["grid_size"]))

    start_x = arguments["grid_size"] // 2
    start_y = arguments["grid_size"] // 2
    grid[start_x, start_y] = 255

    location = Vector(start_x, start_y)
    velocity = Vector(0, 0)
    acceleration = Vector(-0.001, 0.01)

    mover = Mover(grid, arguments["grid_size"], location, velocity,
                  acceleration)

    display = Display(arguments["interval"], arguments["grid_size"])
    display.animate(grid, arguments["interval"], mover.move)


if __name__ == "__main__":
    main()
