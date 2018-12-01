#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pathlib import Path
import unittest

from shared.utils import get_input
from . import solution1, solution2


SOLUTION_DIR = Path(__file__).parent


class TestSolution(unittest.TestCase):
    module = None
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

    def get_input(self, filename):
        input_path = SOLUTION_DIR.joinpath(filename)
        input_text = get_input(input_path)
        return input_text


class TestSolution1(TestSolution):
    module = solution1
    expected = "lorem ipsum!"

    def test_solver(self):
        input_text = self.get_input("test_input.txt")
        solution = self.module.solve(input_text)
        self.assertEqual(self.expected, solution)


class TestSolution2(TestSolution):
    module = solution2
    expected = "lorem ipsum?"

    def test_solver(self):
        input_text = self.get_input("test_input.txt")
        solution = self.module.solve(input_text)
        self.assertEqual(self.expected, solution)


if __name__ == '__main__':
    unittest.main()
