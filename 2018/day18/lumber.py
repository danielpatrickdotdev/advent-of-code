#!/usr/bin/env python
# -*- coding: utf-8 -*-


class LumberCollectionArea:
    def __init__(self, data):
        self.size = len(data)
        self.data = [list(line) for line in data]

    def __str__(self):
        return "\n".join("".join(line) for line in self.data)
