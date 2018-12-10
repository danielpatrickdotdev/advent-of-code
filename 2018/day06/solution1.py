#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pathlib import Path

from .common import complete_grid, get_manhattan_distance, parse


def get_closest_destination(x, y, coords):
    closest = None
    closest_distance = 999  # further than biggest distance possible

    for n, coord in enumerate(coords):
        distance = get_manhattan_distance(x, y, coord)

        if distance == closest_distance:
            closest = None
        elif distance < closest_distance:
            closest_distance = distance
            closest = n

    return closest


def is_bound(n, grid):
    # A terribly naive way to determine this
    for row in grid:
        # n in first column
        if row[0] == n:
            return False

        # n in last column
        if row[-1] == n:
            return False

    # n in first or last row
    if n in grid[0] or n in grid[-1]:
        return False

    return True


def solve(input_text):
    coords = parse(input_text)
    grid = complete_grid(coords, get_closest_destination)
    flat_grid = [cell for row in grid for cell in row]

    biggest_range = 0

    for n in range(len(coords)):
        count = flat_grid.count(n)
        if is_bound(n, grid) and count > biggest_range:
            biggest_range = count

    return biggest_range


if __name__ == '__main__':
    from shared.utils import get_input

    input_path = Path(__file__).parent.joinpath("input.txt")
    input_text = get_input(input_path)
    solution = solve(input_text)
    print(solution)
