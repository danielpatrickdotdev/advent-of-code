#!/usr/bin/env python
# -*- coding: utf-8 -*-

from collections import Counter


class LumberCollectionArea:
    def __init__(self, data):
        self.size = len(data)
        self.data = [list(line) for line in data]

    def in_bounds(self, x, y):
        return x >= 0 and x < self.size and y >= 0 and y < self.size

    def get(self, x, y):
        return self.data[y][x]

    def get_surrounding_square_contents(self, x, y):
        surrounding_squares = [
            (x - 1, y - 1),
            (x, y - 1),
            (x + 1, y - 1),
            (x - 1, y),
            (x + 1, y),
            (x - 1, y + 1),
            (x, y + 1),
            (x + 1, y + 1)
        ]

        surrounding_square_contents = [
            self.get(*square) for square in surrounding_squares
            if self.in_bounds(*square)
        ]

        return Counter(surrounding_square_contents)

    def change_square(self, x, y):
        contents = self.get(x, y)
        surrounding = self.get_surrounding_square_contents(x, y)
        if contents == ".":
            if surrounding["|"] >= 3:
                return "|"
            else:
                return "."
        elif contents == "|":
            if surrounding["#"] >= 3:
                return "#"
            else:
                return "|"
        elif surrounding["#"] >= 1 and surrounding["|"] >= 1:
            return "#"
        else:
            return "."

    def __str__(self):
        return "\n".join("".join(line) for line in self.data)
