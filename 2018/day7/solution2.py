#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pathlib import Path

from .common import get_available, get_steps, parse
from .worker import Worker


def increment_workers(workers):
    completed = []

    for worker in workers:
        char = worker.work()
        if char is not None:
            completed.append(char)

    return completed


def num_available_workers(workers):
    return sum(worker.is_idle() for worker in workers)


def assign_work(workers, char, time):
    assigned = False

    for worker in workers:
        if worker.is_idle():
            worker.work_on(char, time)
            assigned = True
            break

    if not assigned:
        raise Exception("Unable to assign work - everyone's busy")


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
