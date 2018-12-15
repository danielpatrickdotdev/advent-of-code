#!/usr/bin/env python
# -*- coding: utf-8 -*-

from operator import itemgetter


class Caves:
    def __init__(self, data):
        self.grid = []
        self.goblins = []
        self.elves = []

        for x in range(len(data[0])):
            col = []
            self.grid.append(col)

            for y in range(len(data)):
                cell_contents = data[y][x]

                col.append(cell_contents)

                if cell_contents == "G":
                    self.goblins.append((x, y))
                elif cell_contents == "E":
                    self.elves.append((x, y))

        self.sort()

    def sort(self):
        self.elves.sort(key=itemgetter(1, 0))
        self.goblins.sort(key=itemgetter(1, 0))
