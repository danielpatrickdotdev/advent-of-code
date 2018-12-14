#!/usr/bin/env python
# -*- coding: utf-8 -*-

from collections import Counter
from pathlib import Path


def parser(input_text):
    return [line for line in input_text]


def count_repeats(box_ids):
    twos = threes = 0

    for box_id in box_ids:
        counts = Counter(box_id)

        repeats_twice = repeats_thrice = False

        for char in counts:
            if not repeats_twice and counts[char] == 2:
                repeats_twice = True
                twos += 1
            elif not repeats_thrice and counts[char] == 3:
                repeats_thrice = True
                threes += 1

    return twos, threes


def solve(input_text):
    box_ids = parser(input_text)
    twos, threes = count_repeats(box_ids)
    return twos * threes


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
