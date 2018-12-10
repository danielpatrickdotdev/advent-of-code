#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pathlib import Path
from .common import parse, find_time_with_closest_fit
from .rescue import RescueMessage


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
