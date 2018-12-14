#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pathlib import Path

from .common import parse, play_game


def solve(input_text):
    num_players, num_marbles = parse(input_text)
    num_marbles *= 100
    return max(play_game(num_players, num_marbles))


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
