#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pathlib import Path

from .common import get_manhattan_distance


def calculate_distance_from_all_coords(x, y, coords):
    return sum(get_manhattan_distance(x, y, coord) for coord in coords)


def solve(input_text):
    return " ".join(input_text) + "?"


if __name__ == '__main__':
    from shared.utils import get_input

    input_path = Path(__file__).parent.joinpath("input.txt")
    input_text = get_input(input_path)
    solution = solve(input_text)
    print(solution)
