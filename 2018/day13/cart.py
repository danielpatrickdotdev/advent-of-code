#!/usr/bin/env python
# -*- coding: utf-8 -*-

from collections import deque


class Cart:
    moves_map = {
        "^": (0, -1),
        ">": (1, 0),
        "v": (0, 1),
        "<": (-1, 0),
    }
    reorient_map = {
        ("^", "|"): "^",
        ("<", "\\"): "^",
        (">", "/"): "^",
        (">", "-"): ">",
        ("^", "/"): ">",
        ("v", "\\"): ">",
        ("v", "|"): "v",
        (">", "\\"): "v",
        ("<", "/"): "v",
        ("<", "-"): "<",
        ("^", "\\"): "<",
        ("v", "/"): "<",
    }

    def __init__(self, x, y, d):
        self.crashed = False
        self.x = x
        self.y = y
        self.d = d

        self.crossroad_choices = deque([-1, 0, 1])
        self.moves = deque("^>v<")
        self.moves.rotate(4 - self.moves.index(d) - 1)

    def move(self, tracks):
        if self.crashed:
            return

        dx, dy = self.moves_map[self.d]
        self.x += dx
        self.y += dy
        self.reorient(tracks.get(self.x, self.y))

    def reorient(self, new_tile):
        if new_tile == "+":
            self.moves.rotate(self.crossroad_choices[-1])
            self.d = self.moves[-1]
            self.crossroad_choices.rotate(1)
        else:
            self.d = self.reorient_map[self.d, new_tile]
            self.moves.rotate(4 - self.moves.index(self.d) - 1)

    def opposite_dir(self):
        return self.moves[1]

    def has_crashed(self):
        return self.crashed

    def set_crashed(self):
        self.crashed = True

    def __str__(self):
        return "{}, {}, {}".format(self.x, self.y, self.d)
