#!/usr/bin/env Python3

""""""

import matplotlib.animation as ani
import matplotlib.pyplot as plt
import numpy as np


class Display:
    """"""

    def __init__(self, interval, size):
        """"""
        self.interval = interval
        self.size = size

    def animate(self, grid, interval, update, movie_file=None):
        """"""
        figure, axis = plt.subplots()
        image = axis.imshow(grid, interpolation='nearest')
        animation = ani.FuncAnimation(figure, update,
                                      fargs=(image,),
                                      interval=self.interval,
                                      save_count=50)

        # Rewrite how file is saved.
        if movie_file:
            animation.save(movie_file, fps=30,
                           extra_args=['-vcodec', 'libx264'])
     
        plt.show()

    def still(self, grid, image_file=None):
        """"""
        raise NotImplementedError
