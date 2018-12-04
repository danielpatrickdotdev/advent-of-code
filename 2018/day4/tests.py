#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pathlib import Path
import unittest

from shared.utils import get_input
from . import solution1, solution2, common
from .shift import Shift


SOLUTION_DIR = Path(__file__).parent


class TestSolution(unittest.TestCase):
    module = None
    input_filename = "test_input.txt"
    expected = None

    def setUp(self):
        if self.module is None:
            raise NotImplementedError(
                "subclasses of TestSolution must provide module to test"
            )
        if self.expected is None:
            raise NotImplementedError(
                "subclasses of TestSolution must provide expected value"
            )
        self.input_path = SOLUTION_DIR.joinpath(self.input_filename)
        self.input_text = get_input(self.input_path)


class TestShift(unittest.TestCase):
    def test_create_shift_object(self):
        events = {
            25: "wakes up",
            5: "falls asleep",
            55: "wakes up",
            0: "Guard #10 begins shift",
            30: "falls asleep",
        }
        shift = Shift(events)
        self.assertEqual(10, shift.guard_id)
        self.assertEqual(0, shift.shift_started)
        self.assertEqual(45, len(shift.sleeps))
        self.assertEqual(list(range(5, 25)) + list(range(30, 55)), shift.sleeps)


class SleepTimesMixin:
    guard10_sleep_times = [
        5, 6, 7, 8, 9, 10, 11, 12, 13, 14,
        15, 16, 17, 18, 19, 20, 21, 22, 23, 24,
        30, 31, 32, 33, 34, 35, 36, 37, 38, 39,
        40, 41, 42, 43, 44, 45, 46, 47, 48, 49,
        50, 51, 52, 53, 54, 24, 25, 26, 27, 28,
    ]
    guard99_sleep_times = [
        40, 41, 42, 43, 44, 45, 46, 47, 48, 49,
        36, 37, 38, 39, 40, 41, 42, 43, 44, 45,
        45, 46, 47, 48, 49, 50, 51, 52, 53, 54,
    ]


class TestCommon(unittest.TestCase, SleepTimesMixin):
    module = common
    input_as_list = [
        "[1518-11-01 00:00] Guard #10 begins shift",
        "[1518-11-01 00:05] falls asleep",
        "[1518-11-01 00:25] wakes up",
        "[1518-11-01 00:30] falls asleep",
        "[1518-11-01 00:55] wakes up",
        "[1518-11-01 23:58] Guard #99 begins shift",
        "[1518-11-02 00:40] falls asleep",
        "[1518-11-02 00:50] wakes up",
        "[1518-11-03 00:05] Guard #10 begins shift",
        "[1518-11-03 00:24] falls asleep",
        "[1518-11-03 00:29] wakes up",
        "[1518-11-04 00:02] Guard #99 begins shift",
        "[1518-11-04 00:36] falls asleep",
        "[1518-11-04 00:46] wakes up",
        "[1518-11-05 00:03] Guard #99 begins shift",
        "[1518-11-05 00:45] falls asleep",
        "[1518-11-05 00:55] wakes up",
    ]

    def test_parser(self):
        shifts = self.module.parse(self.input_as_list)
        self.assertEqual(5, len(shifts))

        shift1 = shifts[(11, 1)]
        self.assertEqual("Guard #10 begins shift", shift1[0])
        self.assertEqual("falls asleep", shift1[5])
        self.assertEqual("wakes up", shift1[25])
        self.assertEqual("falls asleep", shift1[30])
        self.assertEqual("wakes up", shift1[55])

        shift2 = shifts[(11, 2)]
        self.assertEqual("Guard #99 begins shift", shift2[-2])
        self.assertEqual("falls asleep", shift2[40])
        self.assertEqual("wakes up", shift2[50])

    def test_create_shift_objects(self):
        shift1_events = {
            25: "wakes up",
            55: "wakes up",
            0: "Guard #10 begins shift",
            5: "falls asleep",
            30: "falls asleep",
        }
        shift2_events = {
            40: "falls asleep",
            50: "wakes up",
            -2: "Guard #99 begins shift",
        }
        shift_events = {
            (11, 1): shift1_events,
            (11, 2): shift2_events,
        }

        shifts = self.module.create_shift_objects(shift_events)

        shift1 = shifts[(11, 1)]
        self.assertEqual(10, shift1.guard_id)
        self.assertEqual(0, shift1.shift_started)
        self.assertEqual(45, len(shift1.sleeps))
        self.assertEqual(list(range(5, 25)) + list(range(30, 55)),
                         shift1.sleeps)

        shift2 = shifts[(11, 2)]
        self.assertEqual(99, shift2.guard_id)
        self.assertEqual(-2, shift2.shift_started)
        self.assertEqual(10, len(shift2.sleeps))
        self.assertEqual(list(range(40, 50)), shift2.sleeps)

    def test_guard_sleep_times(self):
        shifts = self.module.create_shift_objects(
            self.module.parse(self.input_as_list)
        )
        sleep_times = self.module.guard_sleep_times(shifts)
        self.assertCountEqual(self.guard10_sleep_times, sleep_times[10])
        self.assertCountEqual(self.guard99_sleep_times, sleep_times[99])


class TestSolution1(TestSolution, SleepTimesMixin):
    module = solution1
    expected = 240

    def test_get_longest_sleeper(self):
        sleep_times = {
            10: self.guard10_sleep_times,
            99: self.guard99_sleep_times,
        }
        self.assertEqual(10, self.module.get_longest_sleeper(sleep_times))

    def test_get_guards_sleepiest_minute(self):
        self.assertEqual(
            24,
            self.module.get_guards_sleepiest_minute(self.guard10_sleep_times)
        )
        self.assertEqual(
            45,
            self.module.get_guards_sleepiest_minute(self.guard99_sleep_times)
        )

    def test_solver(self):
        solution = self.module.solve(self.input_text)
        self.assertEqual(self.expected, solution)


class TestSolution2(TestSolution):
    module = solution2
    expected = 4455

    def test_solver(self):
        solution = self.module.solve(self.input_text)
        self.assertEqual(self.expected, solution)


if __name__ == '__main__':
    unittest.main()
