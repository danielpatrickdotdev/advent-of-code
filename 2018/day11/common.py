#!/usr/bin/env python
# -*- coding: utf-8 -*-


def get_cell_power_level(x, y, serial):
    rack_id = x + 10
    return (((rack_id * y + serial) * rack_id) % 1000) // 100 - 5


def create_grid(serial):
    return [
        [get_cell_power_level(x, y, serial) for y in range(1, 301)]
        for x in range(1, 301)
    ]
