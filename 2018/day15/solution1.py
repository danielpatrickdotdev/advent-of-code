#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pathlib import Path

from .caves import Caves


def solve(input_text):
    caves = Caves(input_text)
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
