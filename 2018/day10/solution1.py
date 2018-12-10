#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pathlib import Path
from .common import parse, find_time_with_closest_fit, advance
from .rescue import RescueMessage


def solve(input_text):
    data = parse(input_text)

    best_time = find_time_with_closest_fit(data[:100])
    advance(data, best_time)
    rescue_message = RescueMessage(data)

    return str(rescue_message)


if __name__ == '__main__':
    from shared.utils import get_input

    input_path = Path(__file__).parent.joinpath("input.txt")
    input_text = get_input(input_path)
    solution = solve(input_text)
    print(solution)
