#!/usr/bin/env python
# -*- coding: utf-8 -*-

from collections import defaultdict
from datetime import date, timedelta
from pathlib import Path
import re

from .common import (
    create_shift_objects,
    get_guards_sleepiest_minute,
    guard_sleep_times,
    parse,
)
from .shift import Shift


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

    input_path = Path(__file__).parent.joinpath("input.txt")
    input_text = get_input(input_path)
    solution = solve(input_text)
    print(solution)
