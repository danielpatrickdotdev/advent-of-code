#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pathlib import Path
import unittest

from shared.utils import get_input
from . import solution1, solution2, common
from .caves import Caves


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

    def test_parser(self):
        depth, target_x, target_y = self.module.parse(
            ["depth: 24680", "target: 12345,67890"]
        )
        self.assertEqual(24680, depth)
        self.assertEqual(12345, target_x)
        self.assertEqual(67890, target_y)


class TestCaves(unittest.TestCase):
    caves_string = (
        "M=.|=.|.|=.\n"
        ".|=|=|||..|\n"
        ".==|....||=\n"
        "=.|....|.==\n"
        "=|..==...=.\n"
        "=||.=.=||=|\n"
        "|.=.===|||.\n"
        "|..==||=.|=\n"
        ".=..===..=|\n"
        ".======|||=\n"
        ".===|=|===T"
    )

    def test_constructor(self):
        caves = Caves(510, 10, 10)
        self.assertEqual(0, caves.get_geology(0, 0))
        self.assertEqual(16_807, caves.get_geology(1, 0))
        self.assertEqual(48_271, caves.get_geology(0, 1))
        self.assertEqual(145_722_555, caves.get_geology(1, 1))
        self.assertEqual(0, caves.get_geology(10, 10))
        self.assertEqual(self.caves_string, str(caves))

    def test_get_geology(self):
        caves = Caves(510, 10, 10)
        self.assertEqual(145_722_555, caves.get_geology(1, 1))

    def test_get_erosion(self):
        caves = Caves(510, 10, 10)
        self.assertEqual(1805, caves.get_erosion(1, 1))

    def test_get_type(self):
        caves = Caves(510, 10, 10)
        self.assertEqual("M", caves.get_type(0, 0))
        self.assertEqual("=", caves.get_type(1, 0))
        self.assertEqual(".", caves.get_type(0, 1))
        self.assertEqual("|", caves.get_type(1, 1))
        self.assertEqual("T", caves.get_type(10, 10))

    def test_get_risk(self):
        caves = Caves(510, 10, 10)
        self.assertEqual(0, caves.get_risk(0, 0))
        self.assertEqual(1, caves.get_risk(1, 0))
        self.assertEqual(0, caves.get_risk(0, 1))
        self.assertEqual(2, caves.get_risk(1, 1))
        self.assertEqual(0, caves.get_risk(10, 10))


class TestSolution1(TestSolution):
    module = solution1
    expected = 114

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
