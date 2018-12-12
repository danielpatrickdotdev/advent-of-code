#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pathlib import Path

from .common import parse
from .plantpots import PlantPots


def solve(input_text):
    plant_state, rules = parse(input_text)
    plantpots = PlantPots(plant_state)

    for n in range(20):
        plantpots = plantpots.advance(rules)

    return plantpots.score()


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
