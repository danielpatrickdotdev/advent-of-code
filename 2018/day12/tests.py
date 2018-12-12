#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pathlib import Path
import unittest
from unittest.mock import patch

from shared.utils import get_input
from . import solution1, solution2, common
from .plantpots import PlantPots


SOLUTION_DIR = Path(__file__).parent


class TestCommon(unittest.TestCase):
    module = common

    def test_parser(self):
        test_input = [
            "initial state: ..#..",
            "",
            "..#.. => #",
            ".###. => #",
            "..... => .",
        ]
        expected_rules = ["..#..", ".###."]

        state, rules = self.module.parse(test_input)

        self.assertEqual("..#..", state)
        self.assertEqual(expected_rules, rules)


class TestPlantPots(unittest.TestCase):
    def test_constructor(self):
        plantpots = PlantPots("#..#..#.")
        self.assertEqual(11, len(plantpots))
        self.assertEqual("..#..#..#..", str(plantpots))
        self.assertEqual(2, plantpots.offset)

    def test_pad_and_trim(self):
        to_test = [
            ("#..", "..#..", 2),
            (".#..", "..#..", 1),
            ("..#..", "..#..", 0),
            ("...#..", "..#..", -1),
            ("....#..", "..#..", -2),
            (".....#..", "..#..", -3),
            ("..#", "..#..", 0),
            ("..#.", "..#..", 0),
            ("..#..", "..#..", 0),
            ("..#...", "..#..", 0),
            ("..#....", "..#..", 0),
            ("..", ".....", 0),
        ]

        for arg, string, offset in to_test:
            plantpots = PlantPots(arg)
            self.assertEqual(string, str(plantpots))
            self.assertEqual(offset, plantpots.offset)

    def test_advance(self):
        rules = {
            "...#.": "#",
            ".#...": "#",
        }

        plantpots = PlantPots("..#..#..")
        new_plantpots = plantpots.advance(rules)
        self.assertEqual("..#....#..", str(new_plantpots))
        self.assertEqual(1, new_plantpots.offset)

    def test__next_get(self):
        plantpots = PlantPots("..#..")
        rules = {
            "..#..": "#",
        }
        self.assertEqual("#", plantpots._next_gen(2, rules))


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
    expected = 325

    def test_solver(self):
        solution = self.module.solve(self.input_text)
        self.assertEqual(self.expected, solution)


class TestSolution2(TestSolution):
    module = solution2
    expected = 325

    def test_solver(self):
        solution = self.module.solve(self.input_text, 20)
        self.assertEqual(self.expected, solution)

    def test_solver_short_circuits_after_finding_match(self):
        more_test_input = [
            "initial state: ..#..",
            "",
            "..#.. => #",
        ]

        with patch.object(PlantPots, "advance",
                          return_value=PlantPots("..#..")) as mock_method:
            solution = self.module.solve(more_test_input, 50_000_000_000)
            self.assertEqual(2, solution)
            self.assertEqual(1, mock_method.call_count)


if __name__ == '__main__':
    unittest.main()
