#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pathlib import Path

from .common import (
    create_shift_objects,
    get_guards_sleepiest_minute,
    guard_sleep_times,
    parse,
)


def get_longest_sleeper(sleep_times):
    longest_asleep = 0
    sleepiest_guard = None

    for guard_id, times in sleep_times.items():
        if len(times) > longest_asleep:
            longest_asleep = len(times)
            sleepiest_guard = guard_id

    return sleepiest_guard


def solve(input_text):
    shifts = create_shift_objects(parse(input_text))
    sleep_times = guard_sleep_times(shifts)

    guard = get_longest_sleeper(sleep_times)
    minute = get_guards_sleepiest_minute(sleep_times[guard])

    return guard * minute


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
    print("Time elapsed: {:.3f}".format(end - start))
