#!/usr/bin/env python
# -*- coding: utf-8 -*-

from math import ceil
from pathlib import Path

from .caves import Caves


def full_battle(input_text, power):
    caves = Caves(input_text)
    for elf in caves.elves:
        elf.attack_power = power

    turns = 0

    while caves.elves and caves.goblins:
        turns += 1
        game_over = caves.advance()
        if game_over:
            turns -= 1
            break

    goblin_points = sum(g.hit_points for g in caves.goblins)
    elf_points = sum(e.hit_points for e in caves.elves)

    return (goblin_points + elf_points) * turns


def try_elf_power(input_text, power):
    caves = Caves(input_text)
    for elf in caves.elves:
        elf.attack_power = power

    starting_elves = len(caves.elves)

    while len(caves.elves) == starting_elves and caves.goblins:
        caves.advance()

    return len(caves.elves) == starting_elves


def get_middle(a, b):
    return ceil((a + b) / 2)


def get_power(input_text):
    start = 0  # too low power
    end = 32  # hopefully too high power

    while not try_elf_power(input_text, end):
        start = end
        end *= 2

    while end > (start + 1):
        mid = get_middle(start, end)

        if try_elf_power(input_text, mid):
            end = mid
        else:
            start = mid

    return get_middle(start, end)


def solve(input_text):
    power = get_power(input_text)

    return full_battle(input_text, power)


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
