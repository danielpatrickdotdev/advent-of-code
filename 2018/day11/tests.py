#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest

from . import solution1, solution2


class TestSolution1(unittest.TestCase):
    module = solution1

    def test_get_cell_power_level(self):
        self.assertEqual(4, self.module.get_cell_power_level(3, 5, 8))
        self.assertEqual(-5, self.module.get_cell_power_level(122, 79, 57))
        self.assertEqual(0, self.module.get_cell_power_level(217, 196, 39))
        self.assertEqual(4, self.module.get_cell_power_level(101, 153, 71))

    def test_create_grid(self):
        grid = self.module.create_grid(18)
        self.assertEqual(300, len(grid))
        self.assertEqual(300, len(grid[0]))
        self.assertEqual([-2, -4, 4, 1, -1], grid[31][43:48])
        self.assertEqual([4, -5, -4, -3, -2], grid[35][43:48])

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
