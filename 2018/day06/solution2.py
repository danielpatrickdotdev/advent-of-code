#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pathlib import Path

from .common import complete_grid, get_manhattan_distance, parse


def calculate_distance_from_all_coords(x, y, coords):
    return sum(get_manhattan_distance(x, y, coord) for coord in coords)


def solve(input_text, n=32):
    coords = parse(input_text)
    grid = complete_grid(coords, calculate_distance_from_all_coords)
    flat_grid = [cell for row in grid for cell in row]

    return len([cell for cell in flat_grid if cell < n])


if __name__ == '__main__':
    from shared.utils import get_input
    from timeit import default_timer as timer

    start = timer()

    input_path = Path(__file__).parent.joinpath("input.txt")
    input_text = get_input(input_path)
    solution = solve(input_text, 10000)
    print(solution)

    end = timer()
    print()
    print("-" * 80)
    print("Time elapsed: {:.3f}".format(end - start))
