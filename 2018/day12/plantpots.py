#!/usr/bin/env python
# -*- coding: utf-8 -*-

from collections import deque


class PlantPots:
    def __init__(self, string, offset=0):
        self.data = deque(string)
        self.offset = offset
        self.pad_and_trim()

    def pad_and_trim(self):
        if self.data[0] == "#":
            self.offset += 2
            self.data.extendleft("..")
        elif self.data[1] == "#":
            self.offset += 1
            self.data.extendleft(".")
        else:
            while len(self.data) > 2 and "#" not in (
                    self.data[0], self.data[1], self.data[2]):
                self.data.popleft()
                self.offset -= 1

        if self.data[-1] == "#":
            self.data.extend("..")
        elif self.data[-2] == "#":
            self.data.extend(".")
        else:
            while len(self.data) > 2 and "#" not in (
                    self.data[-3], self.data[-2], self.data[-1]):
                self.data.pop()

        while len(self.data) < 5:
            self.data.append(".")

    def _next_gen(self, i, rules):
        to_match = "".join(
            self.data[n] if (n >= 0 and n < len(self.data)) else "."
            for n in range(i - 2, i + 3)
        )

        return "#" if to_match in rules else "."

    def advance(self, rules):
        return PlantPots(
            "".join(self._next_gen(i, rules) for i in range(len(self.data))),
            self.offset
        )

    def score(self):
        return sum(
            (i - self.offset)
            for i in range(len(self.data))
            if self.data[i] == "#"
        )

    def __len__(self):
        return len(self.data)

    def __str__(self):
        return "".join(self.data)
