#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pathlib import Path

from .program import Program


def solve(input_text):
    program = Program(input_text, [1, 0, 0, 0, 0, 0])
    program.execute()
    return program.register[0]


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
