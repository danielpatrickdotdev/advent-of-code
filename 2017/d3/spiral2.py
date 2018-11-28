#!/usr/bin/env python3

import sys


class Grid:
    def __init__(self):
        self._grid = [[None for n in range(64)] for n in range(64)]
        self.x = 0
        self.y = 0
        self.dx = 1
        self.dy = 0
        self.n = 1

    def solve(self, target):
        while self.n <= target:
            self.set_n()
            self.move()
            self.update_direction()
            self.update_n()
        return self.n

    def set_n(self):
        self.set(self.x, self.y, self.n)

    def update_direction(self):
        if self.dx and self.get(self.x, self.y + self.dx) is None:
            self.dy = self.dx
            self.dx = 0
        if self.dy and self.get(self.x - self.dy, self.y) is None:
            self.dx = -self.dy
            self.dy = 0

    def update_n(self):
        self.n = self.get_adj()

    def move(self):
        self.x += self.dx
        self.y += self.dy

    def check_coords(self, x, y):
        if abs(x >= 32) or abs(y >= 32):
            raise Exception

    def get(self, x, y):
        self.check_coords(x, y)
        return self._grid[x + 32][y + 32]

    def set(self, x, y, val):
        self.check_coords(x, y)
        self._grid[x + 32][y + 32] = val

    def get_adj(self):
        result = 0
        for x in [self.x - 1, self.x, self.x + 1]:
            for y in [self.y - 1, self.y, self.y + 1]:
                result += self.get(x, y) or 0
        return result


if len(sys.argv) >= 2:
    num = int(sys.argv[1])
    g = Grid()
    print(g.solve(num))
