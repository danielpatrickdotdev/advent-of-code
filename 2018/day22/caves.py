#!/usr/bin/env python
# -*- coding: utf-8 -*-


class Caves:
    cave_risks = {
        "M": 0,
        "T": 0,
        ".": 0,
        "=": 1,
        "|": 2,
    }

    def __init__(self, depth, x, y):
        self.depth = depth
        self.target = (x, y)
        self.create_caverns(x + 1, y + 1)

    def get_geology(self, x, y):
        return self.geology[y][x]

    def get_erosion(self, x, y):
        return self.erosion[y][x]

    def get_type(self, x, y):
        return self.caves[y][x]

    def get_risk(self, x, y):
        return self.cave_risks[self.get_type(x, y)]

    def create_caverns(self, width, height):
        def set_geology(x, y):
            if (x, y) in [(0, 0), self.target]:
                self.geology[-1].append(0)
            elif y == 0:
                self.geology[-1].append(x * 16_807)
            elif x == 0:
                self.geology[-1].append(y * 48_271)
            else:
                self.geology[-1].append(
                    self.get_erosion(x, y - 1) * self.get_erosion(x - 1, y)
                )

        def set_erosion(x, y):
            self.erosion[-1].append(
                (self.get_geology(x, y) + self.depth) % 20_183
            )

        def set_cave_type(x, y):
            cave_types = ".=|"

            if x == y == 0:
                cave_type = "M"  # mouth
            elif (x, y) == self.target:
                cave_type = "T"  # target
            else:
                cave_type = cave_types[self.get_erosion(x, y) % 3]

            self.caves[-1].append(cave_type)

        self.geology = []
        self.erosion = []
        self.caves = []

        for y in range(height):
            self.geology.append([])
            self.erosion.append([])
            self.caves.append([])

            for x in range(width):
                set_geology(x, y)
                set_erosion(x, y)
                set_cave_type(x, y)

    def __str__(self):
        return "\n".join(
            "".join(row) for row in self.caves
        )


class CaveNav:
    def __init__(self, depth, x, y):
        self.caves = Caves(depth, x, y)
