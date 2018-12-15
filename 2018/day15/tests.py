#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pathlib import Path
import unittest

from shared.utils import get_input
from . import solution1, solution2
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


class TestCaves(unittest.TestCase):
    example_input1 = [
        "#########",
        "#G..G..G#",
        "#.......#",
        "#.......#",
        "#G..E..G#",
        "#.......#",
        "#.......#",
        "#G..G..G#",
        "#########",
    ]
    example_cave1 = [
        ["#", "#", "#", "#", "#", "#", "#", "#", "#"],
        ["#", "G", ".", ".", "G", ".", ".", "G", "#"],
        ["#", ".", ".", ".", ".", ".", ".", ".", "#"],
        ["#", ".", ".", ".", ".", ".", ".", ".", "#"],
        ["#", "G", ".", ".", "E", ".", ".", "G", "#"],
        ["#", ".", ".", ".", ".", ".", ".", ".", "#"],
        ["#", ".", ".", ".", ".", ".", ".", ".", "#"],
        ["#", "G", ".", ".", "G", ".", ".", "G", "#"],
        ["#", "#", "#", "#", "#", "#", "#", "#", "#"],
    ]
    example_elves1 = [(4, 4)]
    example_goblins1 = [
        (1, 1), (4, 1), (7, 1), (1, 4), (7, 4), (1, 7), (4, 7), (7, 7)
    ]

    def test_constructor(self):
        caves = Caves(self.example_input1)
        self.assertEqual(self.example_cave1, caves.grid)
        self.assertEqual(self.example_elves1, caves.elves)
        self.assertEqual(self.example_goblins1, caves.goblins)


class TestSolution1(TestSolution):
    module = solution1
    expected = 27730

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
