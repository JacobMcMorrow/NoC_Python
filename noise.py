#!/usr/bin/env python3

"""
h
"""

from abc import ABC, abstractmethod
from math import floor
from random import shuffle


# TODO: Fix documentation, and consider changing names.


# Ken Perlin's original permutation for Perlin Noise. Doubled to work in this
# implementation.
PERMUTATION = [151, 160, 137, 91, 90, 15, 131, 13, 201, 95, 96, 53, 194, 233, 7,
               225, 140, 36, 103, 30, 69, 142, 8, 99, 37, 240, 21, 10, 23, 190,
               6, 148, 247, 120, 234, 75, 0, 26, 197, 62, 94, 252, 219, 203,
               117, 35, 11, 32, 57, 177, 33, 88, 237, 149, 56, 87, 174, 20, 125,
               136, 171, 168, 68, 175, 74, 165, 71, 134, 139, 48, 27, 166, 77,
               146, 158, 231, 83, 111, 229, 122, 60, 211, 133, 230, 220, 105,
               92, 41, 55, 46, 245, 40, 244, 102, 143, 54, 65, 25, 63, 161, 1,
               216, 80, 73, 209, 76, 132, 187, 208, 89, 18, 169, 200, 196, 135,
               130, 116, 188, 159, 86, 164, 100, 109, 198, 173, 186, 3, 64, 52,
               217, 226, 250, 124, 123, 5, 202, 38, 147, 118, 126, 255, 82, 85,
               212, 207, 206, 59, 227, 47, 16, 58, 17, 182, 189, 28, 42, 223,
               183, 170, 213, 119, 248, 152, 2, 44, 154, 163, 70, 221, 153, 101,
               155, 167, 43, 172, 9, 129, 22, 39, 253, 19, 98, 108, 110, 79,
               113, 224, 232, 178, 185, 112, 104, 218, 246, 97, 228, 251, 34,
               242, 193, 238, 210, 144, 12, 191, 179, 162, 241, 81, 51, 145,
               235, 249, 14, 239, 107, 49, 192, 214, 31, 181, 199, 106, 157,
               184, 84, 204, 176, 115, 121, 50, 45, 127, 4, 150, 254, 138, 236,
               205, 93, 222, 114, 67, 29, 24, 72, 243, 141, 128, 195, 78, 66,
               215, 61, 156, 180, 151, 160, 137, 91, 90, 15, 131, 13, 201, 95,
               96, 53, 194, 233, 7, 225, 140, 36, 103, 30, 69, 142, 8, 99, 37,
               240, 21, 10, 23, 190, 6, 148, 247, 120, 234, 75, 0, 26, 197, 62,
               94, 252, 219, 203, 117, 35, 11, 32, 57, 177, 33, 88, 237, 149,
               56, 87, 174, 20, 125, 136, 171, 168, 68, 175, 74, 165, 71, 134,
               139, 48, 27, 166, 77, 146, 158, 231, 83, 111, 229, 122, 60, 211,
               133, 230, 220, 105, 92, 41, 55, 46, 245, 40, 244, 102, 143, 54,
               65, 25, 63, 161, 1, 216, 80, 73, 209, 76, 132, 187, 208, 89, 18,
               169, 200, 196, 135, 130, 116, 188, 159, 86, 164, 100, 109, 198,
               173, 186, 3, 64, 52, 217, 226, 250, 124, 123, 5, 202, 38, 147,
               118, 126, 255, 82, 85, 212, 207, 206, 59, 227, 47, 16, 58, 17,
               182, 189, 28, 42, 223, 183, 170, 213, 119, 248, 152, 2, 44, 154,
               163, 70, 221, 153, 101, 155, 167, 43, 172, 9, 129, 22, 39, 253,
               19, 98, 108, 110, 79, 113, 224, 232, 178, 185, 112, 104, 218,
               246, 97, 228, 251, 34, 242, 193, 238, 210, 144, 12, 191, 179,
               162, 241, 81, 51, 145, 235, 249, 14, 239, 107, 49, 192, 214, 31,
               181, 199, 106, 157, 184, 84, 204, 176, 115, 121, 50, 45, 127, 4,
               150, 254, 138, 236, 205, 93, 222, 114, 67, 29, 24, 72, 243, 141,
               128, 195, 78, 66, 215, 61, 156, 180]


class AbstractNoise(ABC):
    """Abstract class for modeling a variety of different noise classes on."""

    @abstractmethod
    def generate(self):
        pass


class PerlinNoise(AbstractNoise):
    """An implementation of the two dimentional Improved Perlin Noise
    algorithm to generate values according to the input points.

    Details of this implementation and explanations taken from:
    https://rtouti.github.io/graphics/perlin-noise-algorithm

    Original permutations taken from:
    https://en.wikipedia.org/wiki/Perlin_noise

    Private Variables:
    _permuation: List[int] of integers from 0 to 255 inclusive.
    """

    def __init__(self, original_perm=True):
        """Intantiate a new PerlinNoise object. If passed with no arguments
        this instance's permutation table is so to be the original table. If
        <original_perm> is False, a new random permuation table is used."""
        if original_perm:
            self._permutation = PERMUTATION
        else:
            self._permutation = self._make_permutation()

    def _make_permutation(self):
        """Create a permutation table with the integers 0 to 255 in random
        order."""
        permutation = [i for i in range(256)]
        shuffle(permutation)

        # Double the permutations.
        for i in range(256):
            permutation.append(permutation[i])

        return permutation

    def _constant_vector(self, value):
        """Determine the costant unit vector associated with this value from the
        permutation table where <value> is that value.

        Precondition:
            - <value> is an integer from 0 to 255 inclusive.
        """
        h = value & 3

        if h == 0:
            return _VectorTwoD(1.0, 1.0)
        elif h == 1:
            return _VectorTwoD(-1.0, 1.0)
        elif h == 2:
            return _VectorTwoD(-1.0, -1.0)
        else:
            return _VectorTwoD(1.0, -1.0)

    def _fade(self, t):
        """Apply the the fade ease function to <t> to smooth later linear
        interpoation. The fade function is 

                                6t^5 - 15t^4 + 10t^3

        presented in the form bellow to minimize number of multiplications.

        Precondition:
            - <t> must be an integer or floating point number.
        """
        return ((6*t - 15)*t + 10)*t*t*t

    def _lerp(self, t, a1, a2):
        """Perform linear interpolation on <a1> and <a2> for value <t> between
        0.0 and 1.0.

        Precondition:
            - <t>, <a1> and <a2> must be integers or floating point numbers.
        """
        return a1 + t*(a2 - a1)

    def generate(self, x, y):
        """Generate and return the value corresponding to the 2D Perlin Noise
        algoritm at the point corresponding to <x> and <y>.

        Precondition:
            - <x> and <y> must be integers or floating point numbers.
        """
        X = floor(x) & 255
        Y = floor(y) & 255

        xf = x - floor(x)
        yf = y - floor(y)

        # Get the four vectors for our point.
        top_right = _VectorTwoD(xf - 1.0, yf - 1.0)
        top_left = _VectorTwoD(xf, yf - 1.0)
        bot_right = _VectorTwoD(xf - 1.0, yf)
        bot_left = _VectorTwoD(xf, yf)

        # Select a value in the array for each of the 4 corners.
        value_top_right = self._permutation[self._permutation[X + 1] + Y + 1]
        value_top_left = self._permutation[self._permutation[X] + Y + 1]
        value_bot_right = self._permutation[self._permutation[X + 1] + Y]
        value_bot_left = self._permutation[self._permutation[X] + Y]

        # Calculate the dot products with the constant vectors.
        dot_top_right = top_right.dot(self._constant_vector(value_top_right))
        dot_top_left = top_left.dot(self._constant_vector(value_top_left))
        dot_bot_right = bot_right.dot(self._constant_vector(value_bot_right))
        dot_bot_left = bot_left.dot(self._constant_vector(value_bot_left))

        # Calculte the fade function for xf and yf.
        u = self._fade(xf)
        v = self._fade(yf)

        # Return the linear interpolations of the dot products with u and v.
        return self._lerp(u,
                          self._lerp(v, dot_bot_left, dot_top_left),
                          self._lerp(v, dot_bot_right, dot_top_right))


class _VectorTwoD:
    """A two dimensional vector for calculations with the PerlinNoise class."""

    def __init__(self, x, y):
        """Initiate a new _VectorTwoD with <x> as its x value and <y> as its y
        value.
        
        Precondition:
            - <x> and <y> must be integers or floating point numbers.
        """
        self.x = x
        self.y = y

    def dot(self, other):
        """Return the dot product between this vector and <other>, where <other>
        is a two dimentional vector.

        Precondition:
            - <other> must be a two dimentional vector with x and y parameters.

        >>> vector = _VectorTwoD(1, 2)
        >>> other = _VectorTwoD(3, 4)
        >>> vector.dot(other)
        11
        """
        return self.x * other.x + self.y * other.y
