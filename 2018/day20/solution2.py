#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pathlib import Path

from .facility import FacilityMap


def solve(input_text, n=1000):
    facility = FacilityMap(input_text[0])
    return facility.get_rooms_n_doors_away(n)


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
