#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pathlib import Path
import unittest

from shared.utils import get_input
from . import solution1, solution2


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


class TestSolution1(TestSolution):
    module = solution1
    expected = 1
    test_values = [
        [[3, 2, 1, 1], [9, 2, 1, 2], [3, 2, 2, 1]],
        [[5, 3, 4, 6], [10, 7, 1, 1], [5, 7, 4, 6]],
    ]

    def test_parser(self):
        self.assertEqual(self.test_values, self.module.parse(self.input_text))

    def test_solver(self):
        solution = self.module.solve(self.input_text)
        self.assertEqual(self.expected, solution)


class TestSolution2(TestSolution):
    module = solution2
    expected = 0

    def test_solver(self):
        #solution = self.module.solve(self.input_text)
        #self.assertEqual(self.expected, solution)
        pass


if __name__ == '__main__':
    unittest.main()
