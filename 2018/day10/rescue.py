#!/usr/bin/env python
# -*- coding: utf-8 -*-


from collections import defaultdict


class RescueMessage:
    def __init__(self, data):
        self.grid = self.construct_grid()
        self.min_col = None
        self.max_col = None
        self.min_row = None
        self.max_row = None

        for (x, y), (dx, dy) in data:
            if self.min_col is None or x < self.min_col:
                self.min_col = x
            if self.max_col is None or x > self.max_col:
                self.max_col = x
            if self.min_row is None or y < self.min_row:
                self.min_row = y
            if self.max_row is None or y > self.max_row:
                self.max_row = y

            self.grid[y][x].append((dy, dx))

    def construct_grid(self):
        return defaultdict(lambda: defaultdict(list))

    def advance(self, n=1):
        new_grid = self.construct_grid()

        for row_key in self.grid:
            for col_key in self.grid[row_key]:
                cell = self.grid[row_key][col_key]
                while cell:
                    dy, dx = cell.pop()
                    new_row = row_key + dy * n
                    new_col = col_key + dx * n
                    new_grid[new_row][new_col].append((dy, dx))

        self.grid = new_grid

    def __str__(self):
        return "\n".join(
            "".join(
                "#" if self.grid[y][x] else "." for x in range(
                    self.min_col, self.max_col + 1
                )
            ) for y in range(self.min_row, self.max_row +1)
        )

