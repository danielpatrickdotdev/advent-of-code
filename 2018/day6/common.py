#!/usr/bin/env python
# -*- coding: utf-8 -*-


def parse(input_text):
    return [(int(x), int(y)) for x, y in (line.split(", ") for line in input_text)]


def get_max_x_and_y(coords):
    x = max(coord[0] for coord in coords)
    y = max(coord[1] for coord in coords)
    return x, y


def get_manhattan_distance(x, y, coord):
    return abs(x - coord[0]) + abs(y - coord[1])


def get_closest_destination(x, y, coords):
    closest = None
    closest_distance = 999  # further than biggest distance possible

    for n, coord in enumerate(coords):
        distance = get_manhattan_distance(x, y, coord)

        if distance == closest_distance:
            closest = None
        elif distance < closest_distance:
            closest_distance = distance
            closest = n

    return closest
