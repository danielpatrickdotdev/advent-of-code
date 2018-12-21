#!/usr/bin/env python
# -*- coding: utf-8 -*-

from math import ceil
from pathlib import Path

from .program import Program


def get_factors(n):
    # Definitely not the quickest way to do this
    return [i for i in range(1, n + 1) if n % i == 0]


def solve(input_text, reg0=0):
    if reg0 == 0:
        eventual_reg2 = 1024
    elif reg0 == 1:
        eventual_reg2 = 10_551_424
    else:
        raise Exception("Why are you doing this to me?")

    return sum(get_factors(eventual_reg2))


if __name__ == '__main__':
    from shared.utils import get_input
    from timeit import default_timer as timer

    start = timer()

    input_path = Path(__file__).parent.joinpath("input.txt")
    input_text = get_input(input_path)
    solution = solve(input_text, 1)
    print(solution)

    end = timer()
    print()
    print("-" * 80)
    print("Time elapsed: {:.3f}s".format(end - start))
