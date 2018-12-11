#!/usr/bin/env python
# -*- coding: utf-8 -*-


def get_cell_power_level(x, y, serial):
    rack_id = x + 10
    return (((rack_id * y + serial) * rack_id) % 1000) // 100 - 5


def create_grid(serial):
    return [
        [get_cell_power_level(x, y, serial) for y in range(1, 301)]
        for x in range(1, 301)
    ]


def solve(input_value):
    return "{}!".format(input_value)


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
