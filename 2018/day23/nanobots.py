#!/usr/bin/env python
# -*- coding: utf-8 -*-


class Nanobot:
    def __init__(self, x, y, z, r):
        self.x = x
        self.y = y
        self.z = z
        self.r = r

    @property
    def pos(self):
        return (self.x, self.y, self.z)

    @property
    def range(self):
        return self.r

    def in_range(self, other):
        manhattan_distance = sum(
            abs(n1 - n2) for (n1, n2) in zip(self.pos, other.pos)
        )
        return self.range >= manhattan_distance
