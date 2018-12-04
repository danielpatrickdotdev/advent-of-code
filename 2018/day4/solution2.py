#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pathlib import Path
from .common import get_guards_sleepiest_minute


def find_most_consistent_sleeper_and_minute(sleep_times):
    most_times = 0
    most_consistent_guard = None
    guards_most_slept_minute = None

    for guard_id, times in sleep_times.items():
        sleepiest_minute = get_guards_sleepiest_minute(times)
        count = times.count(sleepiest_minute)

        if count > most_times:
            most_times = count
            most_consistent_guard = guard_id
            guards_most_slept_minute = sleepiest_minute

    return (most_consistent_guard, guards_most_slept_minute)


def solve(input_text):
    return " ".join(input_text) + "?"


if __name__ == '__main__':
    from shared.utils import get_input

    input_path = Path(__file__).parent.joinpath("input.txt")
    input_text = get_input(input_path)
    solution = solve(input_text)
    print(solution)
