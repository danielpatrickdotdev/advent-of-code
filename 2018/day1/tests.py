#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pathlib import Path
import unittest

from shared.utils import get_input
from . import solution1, solution2


SOLUTION_DIR = Path(__file__).parent


class TestSolution(unittest.TestCase):
    module = None

    def setUp(self):
        if self.module is None:
            raise NotImplementedError(
                "subclasses of TestSolution must provide module to test"
            )

    def get_input(self, filename):
        input_path = SOLUTION_DIR.joinpath(filename)
        input_text = get_input(input_path)
        return input_text


class TestSolution1(TestSolution):
    module = solution1

    def test_parse_input(self):
        inputs_and_outputs = (
            (0, [1, -2, 3, 1]),
            (1, [1, 1, 1]),
            (2, [1, 1, -2]),
            (3, [-1, -2, -3]),
        )

        for n, expected in inputs_and_outputs:
            input_text = self.get_input("test_input{}.txt".format(n))
            parsed = solution1.parse_input(input_text)
            self.assertEqual(parsed, expected)

    def test_solver_input1(self):
        input_text = self.get_input("test_input0.txt")
        solution = self.module.solve(input_text)
        self.assertEqual(3, solution)

    def test_solver_input2(self):
        input_text = self.get_input("test_input1.txt")
        solution = self.module.solve(input_text)
        self.assertEqual(3, solution)

    def test_solver_input3(self):
        input_text = self.get_input("test_input2.txt")
        solution = self.module.solve(input_text)
        self.assertEqual(0, solution)

    def test_solver_input4(self):
        input_text = self.get_input("test_input3.txt")
        solution = self.module.solve(input_text)
        self.assertEqual(-6, solution)


class TestSolution2(TestSolution):
    module = solution2

    def test_solver_input1(self):
        input_text = self.get_input("test_input0.txt")
        solution = self.module.solve(input_text)
        self.assertEqual(2, solution)

    def test_solver_input4(self):
        input_text = self.get_input("test_input4.txt")
        solution = self.module.solve(input_text)
        self.assertEqual(0, solution)

    def test_solver_input5(self):
        input_text = self.get_input("test_input5.txt")
        solution = self.module.solve(input_text)
        self.assertEqual(10, solution)

    def test_solver_input6(self):
        input_text = self.get_input("test_input6.txt")
        solution = self.module.solve(input_text)
        self.assertEqual(5, solution)

    def test_solver_input7(self):
        input_text = self.get_input("test_input7.txt")
        solution = self.module.solve(input_text)
        self.assertEqual(14, solution)


if __name__ == '__main__':
    unittest.main()
