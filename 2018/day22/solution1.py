#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pathlib import Path

from .common import parse
from .caves import Caves


def solve(input_text):
    depth, *target = parse(input_text)
    caves = Caves(depth, *target)

    width = target[0] + 1
    height = target[1] + 1

    return sum(
        caves.get_risk(x, y) for x in range(width) for y in range(height)
    )


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
