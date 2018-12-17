#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pathlib import Path
import unittest

from shared.utils import get_input
from . import solution1, solution2
from .survey import Survey


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


class DataForTesting:
    test_input = [
        "x=495, y=2..7",
        "y=7, x=495..501",
        "x=501, y=3..7",
        "x=498, y=2..4",
        "x=506, y=1..2",
        "x=498, y=10..13",
        "x=504, y=10..13",
        "y=13, x=498..504",
    ]
    initial_survey = (
        "......+.......\n"
        "............#.\n"
        ".#..#.......#.\n"
        ".#..#..#......\n"
        ".#..#..#......\n"
        ".#.....#......\n"
        ".#.....#......\n"
        ".#######......\n"
        "..............\n"
        "..............\n"
        "....#.....#...\n"
        "....#.....#...\n"
        "....#.....#...\n"
        "....#######..."
    )


class TestSurvey(unittest.TestCase, DataForTesting):
    def setUp(self):
        self.oldMaxDiff = self.maxDiff

    def test_constructor(self):
        self.maxDiff = None
        survey = Survey(self.test_input)
        self.assertEqual(self.initial_survey, str(survey))

    def tearDown(self):
        self.maxDiff = self.oldMaxDiff


class TestSolution1(TestSolution):
    module = solution1
    expected = 57

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
