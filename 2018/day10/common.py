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


def find_time_with_closest_fit(rescue_message):
    intervals = [1000000, 100000, 10000, 1000, 100, 10, 1]

    last_size = rescue_message.size
    new_size = last_size
    best_time = 0

    for interval in intervals:
        # increase by interval unless it makes distance between lights greater
        while new_size <= last_size:
            rescue_message.advance(interval)
            best_time += interval  # track how much we've advanced by

            last_size = new_size
            new_size = rescue_message.size

        rescue_message.advance(-interval)  # reverse to get back to best
        new_size = last_size  # reset new_distance ready for next loop
        best_time -= interval  # track reversed amount

    return best_time
