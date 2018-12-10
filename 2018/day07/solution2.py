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


def assign_jobs_if_possible(workers, requirements, steps, offset):
    available = sorted(list(get_available(requirements, steps)),
                       reverse=True)

    while available and num_available_workers(workers) > 0:
        next_char = available.pop()
        steps.remove(next_char)
        time = time_to_complete_char(next_char, offset)
        assign_work(workers, next_char, time)


def solve(input_text, num_workers=2, offset=0):
    requirements = parse(input_text)
    steps = get_steps(requirements)

    count = 0
    expected_result_len = len(steps)
    result = []
    workers = [Worker() for n in range(num_workers)]

    while len(result) < expected_result_len:
        assign_jobs_if_possible(workers, requirements, steps, offset)

        completed_jobs = increment_workers(workers)

        for char in completed_jobs:
            result.append(char)
            if char in requirements:
                del requirements[char]

        count += 1

    return count


if __name__ == '__main__':
    from shared.utils import get_input

    input_path = Path(__file__).parent.joinpath("input.txt")
    input_text = get_input(input_path)
    solution = solve(input_text, 5, 60)
    print(solution)
