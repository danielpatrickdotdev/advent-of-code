#!/usr/bin/env python
# -*- coding: utf-8 -*-

from functools import reduce
from pathlib import Path


def parse_input(input_text):
    return [int(line) for line in input_text]


def solve(input_text):
    instructions = parse_input(input_text)
    return reduce((lambda acc, item: acc + item), instructions, 0)


if __name__ == '__main__':
    from shared.utils import get_input

    input_path = Path(__file__).parent.joinpath("input.txt")
    input_text = get_input(input_path)
    solution = solve(input_text)
    print(solution)
