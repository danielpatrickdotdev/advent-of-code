#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pathlib import Path
import sys

from .common import parse
from .caves import CaveNav

sys.setrecursionlimit(10_000)


def solve(input_text):
    depth, *target = parse(input_text)
    cavenav = CaveNav(depth, *target)

    return cavenav.get_fastest_route_to_target()


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
