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

    def test_solver(self):
        input_text = self.get_input("test_input1.txt")
        solution = self.module.solve(input_text)
        #self.assertEqual("lorem ipsum?", solution)


if __name__ == '__main__':
    unittest.main()
