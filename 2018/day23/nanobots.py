#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re

nanobot_regex = re.compile("^pos=<(-?\d+),(-?\d+),(-?\d+)>, r=(\d+)$")


def parse_nanobot(string):
    match = nanobot_regex.match(string)
    x, y, z, r = (int(n) for n in match.groups())

    return Nanobot(x, y, z, r)


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
