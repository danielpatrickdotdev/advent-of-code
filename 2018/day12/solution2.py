#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pathlib import Path

from .common import parse
from .plantpots import PlantPots


def solve(input_text, num_generations=20):
    plant_state, rules = parse(input_text)
    plantpots = PlantPots(plant_state)

    first_repeat_gen = None
    prev_plantpots = plantpots

    for n in range(num_generations):
        plantpots = plantpots.advance(rules)

        if str(plantpots) == str(prev_plantpots):
            first_repeat_gen = n
            break

        prev_plantpots = plantpots

    score = plantpots.score()

    if first_repeat_gen is not None:
        remaining_generations = num_generations - first_repeat_gen - 1
        score = score + remaining_generations * (score - prev_plantpots.score())

    return score


if __name__ == '__main__':
    from shared.utils import get_input
    from timeit import default_timer as timer

    start = timer()

    input_path = Path(__file__).parent.joinpath("input.txt")
    input_text = get_input(input_path)
    solution = solve(input_text, 50_000_000_000)
    print(solution)

    end = timer()
    print()
    print("-" * 80)
    print("Time elapsed: {:.3f}s".format(end - start))
