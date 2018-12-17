#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re


regex = re.compile("^([xy])=(\d+), ([xy])=(\d+)\.\.(\d+)$")


class Survey:
    def __init__(self, data):
        to_fill = []
        max_x = min_x = min_y = max_y = None

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

                if min_y is None or range_start < min_y:
                    min_y = range_start

                if max_y is None or range_end > max_y:
                    max_y = range_end

            else:
                if min_y is None or coord1 < min_y:
                    min_y = coord1

                if max_y is None or coord1 > max_y:
                    max_y = coord1

                if min_x is None or range_end < min_x:
                    min_x = range_end

                if max_x is None or range_end > max_x:
                    max_x = range_end

                to_fill.extend(
                    [(x, coord1) for x in range(range_start, range_end + 1)]
                )

        self.width = max_x - min_x + 3
        self.height = max_y + 1

        self.grid = [
            ["." for n in range(self.width)]
            for row in range(self.height)
        ]

        # create clay seams
        for x, y in to_fill:
            self.set(x - min_x + 1, y, "#")

        # add spring
        self.origin = (x, y) = (500 - min_x + 1, 0)
        self.set(x, y, "+")

        # store value as we need it for count_water
        self.min_y = min_y

    def get(self, x, y):
        return self.grid[y][x]

    def set(self, x, y, value):
        self.grid[y][x] = value

    def fill(self, x, y):
        if x == 18 and y == (self.height - 95):
            self.set(x, y - 2, "*")
        x1 = x - 1
        x2 = x + 1
        bound = True  # Has # at both ends

        # Get left boundary of area to fill
        while x1 >= 0 and \
                self.get(x1, y) != "#" and self.get(x1, y + 1) in "#~":
            x1 -= 1

        # Check if bound by clay (#) to the left or empty square (.) below
        if x1 < 0 or self.get(x1, y) != "#":
            bound = False

        # Get right boundary of area to fill
        while x2 < self.width and \
                self.get(x2, y) != "#" and self.get(x2, y + 1) in "#~":
            x2 += 1

        # Check if bound by clay (#) to the right or empty square (.) below
        if x2 >= self.width or self.get(x2, y) != "#":
            bound = False

        if bound:
            # Standing water
            char = "~"
        else:
            # Overflowing
            char = "|"
            if x1 >= 0 and self.get(x1, y) == ".":
                # No clay to the left
                self.set(x1, y, "|")
            if x2 < self.width and self.get(x2, y) == ".":
                # No clay to the right
                self.set(x2, y, "|")

        for x in range(x1 + 1, x2):
            self.set(x, y, char)

        return bound

    def flow(self):
        x, y = self.origin
        y += 1

        while y < self.height:
            reverse = False
            x = 0

            while x < self.width:
                if y == 0:
                    # If we've reversed this far something's probably wrong,
                    # but let's just ignore it for now
                    continue

                if self.get(x, y) == "~":
                    # We're looking at a row we've already filled; ignore
                    pass

                elif self.get(x, y) in ".|" and self.get(x, y - 1) in "+|":
                    # Current square is empty or flowing water and we have
                    # flowing water above
                    if (y + 1) < self.height and self.get(x, y + 1) in "#~":
                        # Clay or standing water is below current square
                        bound = self.fill(x, y)

                        if bound:
                            # the filled area didn't overflow; try to fill
                            # upwards another level
                            reverse = True
                    elif self.get(x, y) == ".":
                        # Nothing stopping donwards flow; keep going
                        self.set(x, y, "|")
                x += 1

            y += -1 if reverse else 1

    def drain(self):
        for y in range(self.height):
            for x in range(self.width):
                if self.get(x, y) == "|":
                    self.set(x, y, ".")

    def count_water(self):
        return sum(
            1 for y in range(
                self.min_y, self.height
            ) for cell in self.grid[y] if cell in "~|"
        )

    def __str__(self):
        return "\n".join("".join(row) for row in self.grid)
