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
    expected = 12
    box_ids = [
        "abcdef",
        "bababc",
        "abbcde",
        "abcccd",
        "aabcdd",
        "abcdee",
        "ababab",
    ]

    def test_parser(self):
        self.assertEqual(self.box_ids, solution1.parser(self.input_text))

    def test_count_repeats(self):
        twos, threes = solution1.count_repeats(self.box_ids)
        self.assertEqual(4, twos)
        self.assertEqual(3, threes)

    def test_solver(self):
        solution = self.module.solve(self.input_text)
        self.assertEqual(self.expected, solution)


class TestSolution2(TestSolution):
    module = solution2
    input_filename = "test_input2.txt"
    expected = "fgij"
    box_ids = [
        "abcde",
        "fghij",
        "klmno",
        "pqrst",
        "fguij",
        "axcye",
        "wvxyz",
    ]

    def test_parser(self):
        self.assertEqual(self.box_ids, solution2.parser(self.input_text))

    def test_count_differences(self):
        self.assertEqual(5, solution2.count_differences(self.box_ids[0],
                                                        self.box_ids[1]))
        self.assertEqual(2, solution2.count_differences(self.box_ids[0],
                                                        self.box_ids[5]))
        self.assertEqual(1, solution2.count_differences(self.box_ids[1],
                                                        self.box_ids[4]))

    def test_find_off_by_one_pair(self):
        self.assertEqual(("fghij", "fguij"),
                         solution2.find_off_by_one_pair(self.box_ids))

    def test_get_matching_letters(self):
        self.assertEqual("", solution2.get_matching_letters(
            self.box_ids[0], self.box_ids[1]))
        self.assertEqual("ace", solution2.get_matching_letters(
            self.box_ids[0], self.box_ids[5]))
        self.assertEqual("fgij", solution2.get_matching_letters(
            self.box_ids[1], self.box_ids[4]))

    def test_solver(self):
        solution = self.module.solve(self.input_text)
        self.assertEqual(self.expected, solution)


if __name__ == '__main__':
    unittest.main()
