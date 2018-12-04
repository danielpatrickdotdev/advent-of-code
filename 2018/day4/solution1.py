#!/usr/bin/env python
# -*- coding: utf-8 -*-

from collections import defaultdict
from datetime import date, timedelta
from pathlib import Path
import re

from .shift import Shift


shift_event_regex = re.compile("^\[1518-(\d{2})-(\d{2}) (\d{2}):(\d{2})\] ("
                               "(?:Guard #\d+ begins shift)|"
                               "(?:falls asleep)|"
                               "(?:wakes up)"
                               ")$")


def parse(input_text):
    shifts = defaultdict(dict)
    for event_string in input_text:
        match = shift_event_regex.match(event_string)
        month, day, hour, minute, event = match.groups()

        month = int(month)
        day = int(day)
        hour = int(hour)
        minute = int(minute)

        if hour == 23:
            shift_date = date(1518, month, day) + timedelta(days=1)
            month = shift_date.month
            day = shift_date.day
            minute = minute - 60

        shifts[(month, day)][minute] = event

    return shifts


def create_shift_objects(shift_events_dict):
    shifts = {}

    for shift_date, shift_events in shift_events_dict.items():
        shifts[shift_date] = Shift(shift_events)

    return shifts


def solve(input_text):
    return " ".join(input_text) + "!"


if __name__ == '__main__':
    from shared.utils import get_input

    input_path = Path(__file__).parent.joinpath("input.txt")
    input_text = get_input(input_path)
    solution = solve(input_text)
    print(solution)
