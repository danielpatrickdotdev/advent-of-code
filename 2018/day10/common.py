#!/usr/bin/env python
# -*- coding: utf-8 -*-


from itertools import combinations
import re


regex = re.compile(
    "position=<([- ]?\d+), ([- ]?\d+)> velocity=<([- ]?\d+), ([- ]?\d+)>"
)


def parse(input_text):
    result = []

    for line in input_text:
        x, y, dx, dy = regex.match(line).groups()
        result.append([(int(x), int(y)), (int(dx), int(dy))])

    return result


def advance(lights, n):
    for light in lights:
        (x, y), (dx, dy) = light
        light[0] = (x + dx * n, y + dy * n)


def get_distance(lights):
    total = 0
    for pair in combinations(lights, 2):
        dx = abs(pair[0][0][0] - pair[1][0][0])
        dy = abs(pair[0][0][1] - pair[1][0][1])
        total += dx + dy

    return total


def find_time_with_closest_fit(lights):
    # make sure we're not modifying original lights object
    lights = [light[:] for light in lights]
    intervals = [1000000, 100000, 10000, 1000, 100, 10, 1]

    last_distance = get_distance(lights)
    new_distance = last_distance
    best_time = 0

    for interval in intervals:
        while new_distance <= last_distance:
            advance(lights, interval)
            best_time += interval

            last_distance = new_distance
            new_distance = get_distance(lights)

        advance(lights, -interval)
        new_distance = last_distance
        best_time -= interval

    return best_time
