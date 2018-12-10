#!/usr/bin/env python
# -*- coding: utf-8 -*-

from itertools import combinations
from pathlib import Path
from .common import parse
from .rescue import RescueMessage


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


def solve(input_text):
    def advance_lights(lights, n):
        for light in lights:
            (y, x), (dy, dx) = light
            light[0] = (y + dy * n, x + dx * n)

    data = parse(input_text)

    best_time = find_time_with_closest_fit(data[:100])
    advance_lights(data, best_time)
    rescue_message = RescueMessage(data)

    return str(rescue_message)


if __name__ == '__main__':
    from shared.utils import get_input

    input_path = Path(__file__).parent.joinpath("input.txt")
    input_text = get_input(input_path)
    solution = solve(input_text)
    print(solution)
