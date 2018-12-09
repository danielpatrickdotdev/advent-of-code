#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pathlib import Path
import unittest

from shared.utils import get_input
from . import solution1, solution2, common


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


class TestCommon(unittest.TestCase):
    module = common
    test_inputs = [
        ["9 players; last marble is worth 25 points"],
        ["10 players; last marble is worth 1618 points"],
        ["13 players; last marble is worth 7999 points"],
        ["17 players; last marble is worth 1104 points"],
        ["21 players; last marble is worth 6111 points"],
        ["30 players; last marble is worth 5807 points"],
        ["458 players; last marble is worth 71307 points"],
    ]
    expected_values = [
        (9, 25),
        (10, 1618),
        (13, 7999),
        (17, 1104),
        (21, 6111),
        (30, 5807),
        (458, 71307),
    ]

    def test_parser(self):
        for test_input, expected in zip(self.test_inputs, self.expected_values):
            self.assertEqual(expected, self.module.parse(test_input))


class TestSolution1(TestSolution):
    module = solution1
    expected = 32
    clockwise_test_values = [
        (0, 1, 1),
        (0, 4, 4),
        (0, 5, 0),
        (1, 3, 4),
        (1, 4, 0),
        (4, 3, 2),
    ]
    test_inputs_and_outputs = [
        (9, 25, 25),
        (10, 1618, 8317),
        (13, 7999, 146373),
        (17, 1104, 2764),
        (21, 6111, 54718),
        (30, 5807, 37305),
    ]

    def test_n_places_clockwise(self):
        circle = [n for n in range(5)]
        for current_value, n, expected in self.clockwise_test_values:
            self.assertEqual(
                expected,
                self.module.n_places_clockwise(circle, current_value, n)
            )

    def test_n_places_counter_clockwise(self):
        circle = [n for n in range(5)]
        for expected, n, current_value in self.clockwise_test_values:
            self.assertEqual(
                expected,
                self.module.n_places_counter_clockwise(circle, current_value, n)
            )

    def test_play_game(self):
        for players, marbles, expected in self.test_inputs_and_outputs:
            self.assertEqual(
                expected,
                max(self.module.play_game(players, marbles))
            )

    def test_solver(self):
        solution = self.module.solve(self.input_text)
        self.assertEqual(self.expected, solution)


class TestSolution2(TestSolution):
    module = solution2
    expected = "lorem ipsum?"

    def test_solver(self):
        solution = self.module.solve(self.input_text)
        self.assertEqual(self.expected, solution)


if __name__ == '__main__':
    unittest.main()
