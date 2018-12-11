#!/usr/bin/env python
# -*- coding: utf-8 -*-


from .common import create_grid, get_squares_power


def get_best_square(grid):
    best_power = 0
    best_x = None
    best_y = None

    for x in range(298):
        for y in range(298):
            power = get_squares_power(x, y, grid)
            if power > best_power:
                best_power = power
                best_x = x
                best_y = y

    return (best_x + 1, best_y + 1)


def solve(input_value):
    grid = create_grid(input_value)
    x, y = get_best_square(grid)

    return "{},{}".format(x, y)


if __name__ == '__main__':
    from timeit import default_timer as timer

    start = timer()

    input_value = 9798
    solution = solve(input_value)
    print(solution)

    end = timer()
    print()
    print("-" * 80)
    print("Time elapsed: {:.3f}s".format(end - start))
