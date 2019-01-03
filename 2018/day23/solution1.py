#!/usr/bin/env python
# -*- coding: utf-8 -*-

from operator import attrgetter
from pathlib import Path

from .nanobots import parse_nanobot


def solve(input_text):
    bots = [parse_nanobot(line) for line in input_text]
    largest = max(bots, key=attrgetter("range"))
    return sum(largest.in_range(*bot.pos) for bot in bots)


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
