#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pathlib import Path

from .common import get_available, get_steps, parse


def increment_workers(workers):
    for worker in workers:
        worker.work()


def time_to_complete_char(char, offset):
    return ord(char) - 64 + offset


def solve(input_text, num_workers=2, offset=0):
    return " ".join(input_text) + "?"


if __name__ == '__main__':
    from shared.utils import get_input

    input_path = Path(__file__).parent.joinpath("input.txt")
    input_text = get_input(input_path)
    solution = solve(input_text, 5, 60)
    print(solution)
