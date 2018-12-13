#!/usr/bin/env python
# -*- coding: utf-8 -*-


class Tracks:
    def __init__(self, initial_data):
        self.data = [row[:] for row in initial_data]

    def get(self, x, y):
        return self.data[y][x]
