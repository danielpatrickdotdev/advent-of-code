#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest

from . import solution1, solution2


class TestSolution1(unittest.TestCase):
    module = solution1

    def test_solver(self):
        self.assertEqual(29, self.module.solve(18))
        self.assertEqual(30, self.module.solve(42))


class TestSolution2(unittest.TestCase):
    module = solution2
    expected = "?"

    def test_solver(self):
        solution = self.module.solve("!")
        self.assertEqual(self.expected, solution)


if __name__ == '__main__':
    unittest.main()
