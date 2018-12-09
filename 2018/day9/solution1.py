#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pathlib import Path

def n_places_clockwise(circle, current_marble, n):
    current_marble += n
    current_marble %= len(circle)
    return current_marble


def n_places_counter_clockwise(circle, current_marble, n):
    current_marble -= n
    current_marble %= len(circle)
    return current_marble


def place_marble(circle, current_marble_pos, next_marble):
    current_marble_pos = n_places_clockwise(
        circle, current_marble_pos, 1) + 1
    if current_marble_pos == len(circle):
        circle.append(next_marble)
    else:
        circle.insert(current_marble_pos, next_marble)

    return circle, current_marble_pos


def solve(input_text):
    return " ".join(input_text) + "!"


if __name__ == '__main__':
    from shared.utils import get_input

    input_path = Path(__file__).parent.joinpath("input.txt")
    input_text = get_input(input_path)
    solution = solve(input_text)
    print(solution)
