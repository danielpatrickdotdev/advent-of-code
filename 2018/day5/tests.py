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
        self.input_text = get_input(self.input_path)[0]


class TestCommon(unittest.TestCase):
    module = common

    def test_check_trigger(self):
        self.assertTrue(self.module.check_trigger("a", "A"))
        self.assertTrue(self.module.check_trigger("Z", "z"))

        self.assertFalse(self.module.check_trigger("a", "a"))
        self.assertFalse(self.module.check_trigger("Z", "Z"))
        self.assertFalse(self.module.check_trigger("a", "Z"))
        self.assertFalse(self.module.check_trigger("A", "z"))

    def test_remove_triggered_pairs(self):
        result = self.module.remove_triggered_pairs("dabAcCaCBAcCcaDA")
        self.assertEqual("dabAaCBAcaDA", result)

        result = self.module.remove_triggered_pairs(result)
        self.assertEqual("dabCBAcaDA", result)

        result = self.module.remove_triggered_pairs(result)
        self.assertEqual("dabCBAcaDA", result)

        # check match at end handled correctly by implementation's loop
        result = self.module.remove_triggered_pairs("aAbaAAa")
        self.assertEqual("b", result)


class TestSolution1(TestSolution):
    module = solution1
    expected = 10

    def test_solver(self):
        solution = self.module.solve(self.input_text)
        self.assertEqual(self.expected, solution)


class TestSolution2(TestSolution):
    module = solution2
    expected = 4

    def test_get_unit_types(self):
        unit_types = self.module.get_unit_types("dabAcCaCBAcCcaDA")
        self.assertCountEqual("ABCD", unit_types)

    def test_remove_unit_type(self):
        result = self.module.remove_unit_type("A", "dabAcCaCBAcCcaDA")
        self.assertEqual(result, "dbcCCBcCcD")

        result = self.module.remove_unit_type("B", "dabAcCaCBAcCcaDA")
        self.assertEqual(result, "daAcCaCAcCcaDA")

        result = self.module.remove_unit_type("C", "dabAcCaCBAcCcaDA")
        self.assertEqual(result, "dabAaBAaDA")

        result = self.module.remove_unit_type("D", "dabAcCaCBAcCcaDA")
        self.assertEqual(result, "abAcCaCBAcCcaA")

    def test_react_polymer(self):
        result = self.module.react_polymer("dabAcCaCBAcCcaDA")
        self.assertEqual(result, "dabCBAcaDA")

    def test_solver(self):
        solution = self.module.solve(self.input_text)
        self.assertEqual(self.expected, solution)


if __name__ == '__main__':
    unittest.main()
