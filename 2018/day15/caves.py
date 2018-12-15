#!/usr/bin/env python
# -*- coding: utf-8 -*-

from operator import itemgetter


class ElfOrGoblin:
    def __init__(self, x, y):
        self.is_dead = False
        self.hit_points = 200
        self.attack_power = 3
        self.x = x
        self.y = y

    def move(self, x, y):
        self.x = x
        self.y = y

    def damage(self, power):
        self.hit_points = max(0, self.hit_points - power)
        self.is_dead = self.hit_points == 0

    def attack(self, other):
        other.damage(self.attack_power)


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
