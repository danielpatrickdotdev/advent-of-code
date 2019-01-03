#!/usr/bin/env python
# -*- coding: utf-8 -*-

from operator import attrgetter, itemgetter
from pathlib import Path

from .nanobots import parse_nanobot


def distance_from_origin(pos):
    return sum(abs(n1 - n2) for (n1, n2) in zip(pos, (0, 0, 0)))


def bots_in_range(bots, x, y, z):
    return sum(bot.in_range(x, y, z) for bot in bots)


def solve(input_text):
    bots = [parse_nanobot(line) for line in input_text]

    # Calculate the best position of those the bots are in - we'll aim to better
    # this
    num_bots_in_range = [[bots_in_range(bots, *bot.pos), bot] for bot in bots]
    best_num_bots, best_bot = max(num_bots_in_range, key=itemgetter(0))
    best_pos = best_bot.pos
    best_distance = distance_from_origin(best_pos)

    # Sort bots on each axis and create ranges of x, y, z coordinates
    x_bots = sorted(bots, key=attrgetter("x"))
    y_bots = sorted(bots, key=attrgetter("y"))
    z_bots = sorted(bots, key=attrgetter("z"))
    x_range = range(x_bots[0].x, x_bots[-1].x + 1)
    y_range = range(y_bots[0].y, y_bots[-1].y + 1)
    z_range = range(z_bots[0].z, z_bots[-1].z + 1)

    # Iterate through all positions in the region, updating our best_ variables
    # when we discover an improved coordinate
    # TODO: Find a much more efficient approach than this!
    for x in x_range:
        for y in y_range:
            for z in z_range:
                num = bots_in_range(bots, x, y, z)
                distance = distance_from_origin((x, y, z))

                if num > best_num_bots or (num == best_num_bots
                                           and distance < best_distance):
                    best_num_bots = num
                    best_pos = (x, y, z)
                    best_distance = distance

    return distance_from_origin(best_pos)


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
