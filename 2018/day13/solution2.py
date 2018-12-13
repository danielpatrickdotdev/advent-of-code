#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pathlib import Path

from .common import move_carts, parse


def solve(input_text):
    tracks, carts = parse(input_text)

    while True:
        move_carts(carts, tracks)

        carts = [cart for cart in carts if not cart.has_crashed()]

        if len(carts) == 1:
            break

    return "{},{}".format(carts[0].x, carts[0].y)


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
