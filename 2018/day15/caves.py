#!/usr/bin/env python
# -*- coding: utf-8 -*-

from operator import attrgetter


class CombatantBaseClass:
    letter = None

    def __init__(self, x, y):
        self.is_dead = False
        self.hit_points = 200
        self.attack_power = 3
        self.x = x
        self.y = y

    def get_location(self):
        return (self.x, self.y)

    def move(self, x, y):
        self.x = x
        self.y = y

    def damage(self, power):
        self.hit_points = max(0, self.hit_points - power)
        self.is_dead = self.hit_points == 0

    def attack(self, other):
        other.damage(self.attack_power)

    def __str__(self):
        return self.letter


class Elf(CombatantBaseClass):
    letter = "E"


class Goblin(CombatantBaseClass):
    letter = "G"


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


                if cell_contents == "G":
                    new_goblin = Goblin(x, y)
                    self.goblins.append(new_goblin)
                    col.append(new_goblin)
                elif cell_contents == "E":
                    new_elf = Elf(x, y)
                    self.elves.append(new_elf)
                    col.append(new_elf)
                else:
                    col.append(cell_contents)

        self.sort()

    def sort(self):
        self.elves.sort(key=attrgetter("y", "x"))
        self.goblins.sort(key=attrgetter("y", "x"))

    def __str__(self):
        return "\n".join(
            "".join(str(item) for item in row) for row in self.grid
        )
