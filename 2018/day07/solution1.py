#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pathlib import Path

from .common import get_available, get_steps, parse


def solve(input_text):
    requirements = parse(input_text)
    steps = get_steps(requirements)

    result = []

    while len(steps) > 0:
        available = get_available(requirements, steps)
        next_char = sorted(list(available))[0]
        steps.remove(next_char)
        if next_char in requirements:
            del requirements[next_char]
        result.append(next_char)

    return "".join(result)


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
    print("Time elapsed: {:.3f}".format(end - start))
