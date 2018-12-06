#!/usr/bin/env python
# -*- coding: utf-8 -*-


def parse(input_text):
    return [(int(x), int(y)) for x, y in (line.split(", ") for line in input_text)]


def get_max_x_and_y(coords):
    x = max(coord[0] for coord in coords)
    y = max(coord[1] for coord in coords)
    return x, y


def create_empty_grid(coords):
    max_x, max_y = get_max_x_and_y(coords)
    horizontal_len = max_x + round(max_x / 10)
    vertical_len = max_y + round(max_y / 10)

    return [[None for n in range(vertical_len)] for n in range(horizontal_len)]
