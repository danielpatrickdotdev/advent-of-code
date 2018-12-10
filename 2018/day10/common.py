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


def find_time_with_closest_fit(lights):
    lights = [light[:] for light in lights]
    intervals = [1000000, 100000, 10000, 1000, 100, 10, 1]

    def get_distance(lights):
        total = 0
        for pair in combinations(lights, 2):
            total += abs(pair[0][0][0] - pair[1][0][0])

        return total

    def advance_lights_y_only(lights, n):
        for light in lights:
            (y, x), (dy, dx) = light
            light[0] = (y + dy * n, x)

    last_distance = get_distance(lights)
    new_distance = last_distance
    best_time = 0

    for interval in intervals:
        while new_distance <= last_distance:
            advance_lights_y_only(lights, interval)
            best_time += interval

            last_distance = new_distance
            new_distance = get_distance(lights)

        advance_lights_y_only(lights, -interval)
        new_distance = last_distance
        best_time -= interval

    return best_time
