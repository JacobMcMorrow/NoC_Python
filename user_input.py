#!/usr/bin/env python3

""""""

# TODO: Fix all the damn documentation.
# TODO: Update for multiple different programs to run.

import argparse


class UserInput:
    """"""

    # Consider passing default values from main().
    def __init__(self):
        """"""
        # Initialize arguments with default values.
        self.arguments = {
            "grid_size":  100,
            "interval":   50,
            "movie_file": None,
        }

    # TODO: Add check if arguments have already been parsed.
    def get_arguments(self):
        """"""
        # parse arguments
        # TODO: Replace description.
        description = "Runs Nature of Code Python equivalents."
        parser = argparse.ArgumentParser(description=description)

        # add arguments
        parser.add_argument('--grid-size', dest='grid_size', required=False)
        parser.add_argument('--movie-file', dest='movie_file', required=False)
        parser.add_argument('--interval', dest='interval', required=False)
        # parser.add_argument('--glider', action='store_true', required=False)
        # parser.add_argument('--gosper', action='store_true', required=False)
        args = parser.parse_args()

        self._check_values(args)

        return self.arguments

    def _check_values(self, args):
        """"""
        # Add error checks for invalid sizes.
        if args.grid_size and int(args.grid_size) > 8:
            self.arguments["grid_size"] = int(args.grid_size)

        # Add error checks for invalid intervals. Make minimun interval reasonable.
        if args.interval and int(args.interval) > 0:
            self.arguments["interval"] = int(args.interval)

        # Add checks for file extension.
        if args.movie_file:
            self.arguments["movie_file"] = args.movie_file
