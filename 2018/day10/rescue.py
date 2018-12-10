#!/usr/bin/env python
# -*- coding: utf-8 -*-


from collections import defaultdict


class RescueMessage:
    def __init__(self, data):
        self.grid = self.construct_grid()
        self.set_boundaries(data)

        for (x, y), (dx, dy) in data:
            self.grid[y][x].append((dy, dx))

    def set_boundaries(self, data):
        self.reset_boundaries()
        for (x, y), (dx, dy) in data:
            self.update_x_boundaries(x)
            self.update_y_boundaries(y)

    def reset_boundaries(self):
        self.min_col = None
        self.max_col = None
        self.min_row = None
        self.max_row = None

    def update_x_boundaries(self, x):
        if self.min_col is None or x < self.min_col:
            self.min_col = x
        if self.max_col is None or x > self.max_col:
            self.max_col = x

    def update_y_boundaries(self, y):
        if self.min_row is None or y < self.min_row:
            self.min_row = y
        if self.max_row is None or y > self.max_row:
            self.max_row = y

    def construct_grid(self):
        return defaultdict(lambda: defaultdict(list))

    def __str__(self):
        return "\n".join(
            "".join(
                "#" if self.grid[y][x] else "." for x in range(
                    self.min_col, self.max_col + 1
                )
            ) for y in range(self.min_row, self.max_row + 1)
        )
