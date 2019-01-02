#!/usr/bin/env python
# -*- coding: utf-8 -*-

from collections import defaultdict
import math


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

    def set_geology(self, x, y):
        if (x, y) in [(0, 0), self.target]:
            self.geology[y][x] = 0
        elif y == 0:
            self.geology[y][x] = x * 16_807
        elif x == 0:
            self.geology[y][x] = y * 48_271
        else:
            self.geology[y][x] = self.get_erosion(
                x, y - 1) * self.get_erosion(x - 1, y)

    def set_erosion(self, x, y):
        self.erosion[y][x] = (self.get_geology(x, y) + self.depth) % 20_183

    def set_cave_type(self, x, y):
        cave_types = ".=|"

        if x == y == 0:
            cave_type = "M"  # mouth
        elif (x, y) == self.target:
            cave_type = "T"  # target
        else:
            cave_type = cave_types[self.get_erosion(x, y) % 3]

        self.caves[y][x] = cave_type

    def create_caverns(self, width, height):
        self.geology = defaultdict(lambda: defaultdict(lambda: None))
        self.erosion = defaultdict(lambda: defaultdict(lambda: None))
        self.caves = defaultdict(lambda: defaultdict(lambda: None))

        for y in range(height):
            for x in range(width):
                self.set_geology(x, y)
                self.set_erosion(x, y)
                self.set_cave_type(x, y)

    def __str__(self):
        return "\n".join(
            "".join(row.values()) for row in self.caves.values()
        )


class CaveNav:
    cave_equipment = {
        "M": ["C", "T"],
        "T": ["C", "T"],
        ".": ["C", "T"],
        "=": ["C", "N"],
        "|": ["T", "N"],
    }

    def __init__(self, depth, x, y):
        self.caves = Caves(depth, x, y)
        self.routes = defaultdict(dict)

    def get_neighbouring_caves(self, x, y):
        neighbours = [
            (x, y - 1),  # up
            (x, y + 1),  # down
            (x - 1, y),  # left
            (x + 1, y),  # right
        ]

        height = len(self.caves.caves)
        width = len(self.caves.caves[0])

        return set(
            (x, y) for (x, y) in neighbours
            if 0 <= x < width and 0 <= y < height
        )

    def get_valid_equipment(self, x, y):
        return self.cave_equipment[self.caves.get_type(x, y)]

    def get_fastest_routes(self, x, y):
        return self.routes[(x, y)]

    def update_fastest_routes(self, x, y):
        updated = False

        equipment1, equipment2 = self.get_valid_equipment(x, y)
        fastest1 = fastest2 = math.inf

        # If this is the Mouth, return early
        if x == y == 0:
            self.routes[(x, y)] = {"C": 7, "T": 0}
            return

        # Get best neighbouring times for valid equipments
        for neighbour in self.get_neighbouring_caves(x, y):
            for equip, minutes in self.get_fastest_routes(*neighbour).items():

                if equipment1 == equip:
                    fastest1 = min(fastest1, minutes + 1)
                elif equipment2 == equip:
                    fastest2 = min(fastest2, minutes + 1)

        # Fastest route may involve changing equipment after moving, also filter
        # out equipment for which we have no route (fastest == math.inf)
        fastest = {eq: f for (eq, f) in [
            (equipment1, min(fastest1, fastest2 + 7)),
            (equipment2, min(fastest2, fastest1 + 7))
        ]
            if f is not math.inf
        }

        # Compare to previously calculated routes, if they exist
        current_routes = self.get_fastest_routes(x, y)

        for equip, minutes in fastest.items():
            if equip in current_routes:
                if current_routes[equip] > minutes:
                    current_routes[equip] = minutes
                    updated = True
            else:
                updated = True
                current_routes[equip] = minutes

        # If we've updated/added times for any equipment on this square, check
        # neighbouring squares that have already been completed and update if
        # this provides a quicker route
        if updated:
            for neighbour in self.get_neighbouring_caves(x, y):
                if neighbour in self.routes and self.routes[neighbour] != {}:
                    self.update_fastest_routes(*neighbour)
