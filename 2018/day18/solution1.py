#!/usr/bin/env python
# -*- coding: utf-8 -*-

from collections import Counter
from pathlib import Path

from .lumber import LumberCollectionArea

def solve(input_text):
    area = LumberCollectionArea(input_text)
    for n in range(10):
        area.update_squares()

    counts = Counter(str(area))
    return counts["|"] * counts["#"]


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
