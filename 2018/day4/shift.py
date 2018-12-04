#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re


class Shift:
    begin_shift_regex = re.compile("^Guard #(\d+) begins shift$")

    def __init__(self, event_dict):
        times = sorted(event_dict.keys())
        sleep_stack = []
        self.sleeps = []

        for time in times:
            event = event_dict[time]
            if event == "falls asleep":
                sleep_stack.append(time)
            elif event == "wakes up":
                self.sleeps += list(range(sleep_stack.pop(), time))
            else:
                self.shift_started = time
                self.guard_id = self.parse_guard_id(event)

    def parse_guard_id(self, string):
        match = self.begin_shift_regex.match(string)
        guard_id, = match.groups()
        return int(guard_id)
