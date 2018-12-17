#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re


regex = re.compile("^([xy])=(\d+), ([xy])=(\d+)\.\.(\d+)$")


class Survey:
    def __init__(self, data):
        to_fill = []
        max_x = min_x = max_y = None

        for line in data:
            match = regex.match(line)
            axis1, coord1, axis2, range_start, range_end = match.groups()
            coord1 = int(coord1)
            range_start = int(range_start)
            range_end = int(range_end)

            if range_start > range_end:
                raise Exception("You've got to be shitting me, "
                                "I've not prepared for that")

            if axis1 == "x":
                to_fill.extend(
                    [(coord1, y) for y in range(range_start, range_end + 1)]
                )

                if max_x is None or coord1 > max_x:
                    max_x = coord1

                if min_x is None or coord1 < min_x:
                    min_x = coord1

                if max_y is None or range_end > max_y:
                    max_y = range_end

            else:
                if max_y is None or coord1 > max_y:
                    max_x = coord1

                if min_x is None or range_end < min_x:
                    min_x = range_end

                if max_x is None or range_end > max_x:
                    max_x = range_end

                to_fill.extend(
                    [(x, coord1) for x in range(range_start, range_end + 1)]
                )

        self.grid = [
            ["." for n in range(max_x - min_x + 3)]
            for row in range(max_y + 1)
        ]

        # create clay seams
        for x, y in to_fill:
            self.grid[y][x - min_x + 1] = "#"

        # add spring
        self.origin = (x, y) = (500 - min_x + 1, 0)
        self.grid[y][x] = "+"

    def __str__(self):
        return "\n".join("".join(row) for row in self.grid)
