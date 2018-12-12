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

        if interval == 1:
            rescue_message.advance(-interval)
            best_time -= interval
            break

        rescue_message.advance(-(interval * 2))  # reverse to get back to best
        new_size = rescue_message.size  # reset new_size
        last_size = new_size
        best_time -= (interval * 2)  # track reversed amount

    return best_time
