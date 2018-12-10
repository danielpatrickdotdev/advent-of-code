#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pathlib import Path

from .common import parse, find_time_with_closest_fit
from .rescue import RescueMessage


def solve(input_text):
    data = parse(input_text)
    rescue_message = RescueMessage(data)

    find_time_with_closest_fit(rescue_message)

    return str(rescue_message)


if __name__ == '__main__':
    from shared.utils import get_input
    from timeit import default_timer as timer

    start = timer()

    input_path = Path(__file__).parent.joinpath("input.txt")
    input_text = get_input(input_path)
    solution = solve(input_text)
    print(solution)

    end = timer()
    print()
    print("-" * 80)
    print("Time elapsed: {:.3f}s".format(end - start))
