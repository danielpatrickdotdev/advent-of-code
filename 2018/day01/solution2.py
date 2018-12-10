#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pathlib import Path

from .solution1 import parse_input


def solve(input_text):
    instructions = parse_input(input_text)
    frequencies = set([0])

    freq = 0
    while True:
        for delta in instructions:
            freq += delta

            if freq in frequencies:
                return freq

            frequencies.add(freq)


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
    print("Time elapsed: {:.3f}".format(end - start))
