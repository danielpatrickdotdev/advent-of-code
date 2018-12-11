#!/usr/bin/env python
# -*- coding: utf-8 -*-


from .common import create_grid


def get_squares_power(x, y, grid, size=3):
    power = 0

    for dx in range(size):
        for dy in range(size):
            power += grid[x + dx][y + dy]

    return power


def get_best_square(grid):
    best_power = 0
    best_x = None
    best_y = None
    best_size = None


    for size in range(1, 301):
        print(size)
        for x in range(300):
            if (size + x) > 300:
                break
            for y in range(300):
                if (size + y) > 300:
                    break
                power = get_squares_power(x, y, grid, size)
                if power > best_power:
                    best_power = power
                    best_x = x
                    best_y = y
                    best_size = size

        if size > (best_size + 5):
            # accept we're probably not going to improve
            # yes, this is terribly naive
            break

    return (best_x + 1, best_y + 1, best_size)


def solve(input_value):
    grid = create_grid(input_value)
    x, y, size = get_best_square(grid)

    return "{},{},{}".format(x, y, size)


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
