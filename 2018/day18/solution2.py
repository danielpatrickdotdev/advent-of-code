#!/usr/bin/env python
# -*- coding: utf-8 -*-

from collections import Counter
from pathlib import Path

from .lumber import LumberCollectionArea


def score(area):
    counts = Counter(str(area))
    return counts["|"] * counts["#"]


def solve(input_text):
    area = LumberCollectionArea(input_text)

    previous_areas = []
    repeated = False
    n = 0

    while n < 1_000_000_000:
        area.update_squares()

        if not repeated:
            string = str(area)
            if string in previous_areas:
                repeated = True
                repeats_after = n - previous_areas.index(string)
                remaining = 1_000_000_000 - n
                advance_by = (remaining // repeats_after) * repeats_after
                n += advance_by
            else:
                previous_areas.append(string)

        n += 1

    return score(area)


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
