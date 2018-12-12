#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest

from . import solution1, solution2, common


class TestCommon(unittest.TestCase):
    module = common

    def test_get_cell_power_level(self):
        self.assertEqual(4, self.module.get_cell_power_level(3, 5, 8))
        self.assertEqual(-5, self.module.get_cell_power_level(122, 79, 57))
        self.assertEqual(0, self.module.get_cell_power_level(217, 196, 39))
        self.assertEqual(4, self.module.get_cell_power_level(101, 153, 71))


class TestSolution1(unittest.TestCase):
    module = solution1

    def test_create_grid(self):
        grid = self.module.create_grid(18)
        self.assertEqual(300, len(grid))
        self.assertEqual(300, len(grid[0]))
        self.assertEqual([-2, -4, 4, 1, -1], grid[31][43:48])
        self.assertEqual([4, -5, -4, -3, -2], grid[35][43:48])

    def test_get_squares_power(self):
        grid = self.module.create_grid(18)
        self.assertEqual(12, self.module.get_squares_power(31, 43, grid))
        self.assertEqual(26, self.module.get_squares_power(32, 43, grid))
        self.assertEqual(29, self.module.get_squares_power(32, 44, grid))
        self.assertEqual(113, self.module.get_squares_power(89, 268, grid, 16))

        grid = self.module.create_grid(42)
        self.assertEqual(119, self.module.get_squares_power(231, 250, grid, 12))

    def test_get_best_square(self):
        self.assertEqual(
            (33, 45),
            self.module.get_best_square(self.module.create_grid(18))
        )
        self.assertEqual(
            (21, 61),
            self.module.get_best_square(self.module.create_grid(42))
        )

    def test_solver(self):
        self.assertEqual("33,45", self.module.solve(18))
        self.assertEqual("21,61", self.module.solve(42))


class TestSolution2(unittest.TestCase):
    module = solution2

    def test_create_optimised_grid(self):
        grid = self.module.create_optimised_grid(18)
        self.assertEqual(300, len(grid))
        self.assertEqual(300, len(grid[0]))
        self.assertEqual(-5, grid[1][1])

    def test_get_squares_power(self):
        grid = self.module.create_optimised_grid(18)
        self.assertEqual(-5, self.module.get_squares_power(0, 0, grid, 2))
        self.assertEqual(-2, self.module.get_squares_power(0, 0, grid, 1))
        self.assertEqual(0, self.module.get_squares_power(1, 1, grid, 1))
        self.assertEqual(-2, self.module.get_squares_power(31, 43, grid, 1))
        self.assertEqual(12, self.module.get_squares_power(31, 43, grid))
        self.assertEqual(26, self.module.get_squares_power(32, 43, grid))
        self.assertEqual(29, self.module.get_squares_power(32, 44, grid))
        self.assertEqual(113, self.module.get_squares_power(89, 268, grid, 16))

        grid = self.module.create_optimised_grid(42)
        self.assertEqual(119, self.module.get_squares_power(231, 250, grid, 12))

    def test_get_best_square(self):
        self.assertEqual(
            (90, 269, 16),
            self.module.get_best_square(self.module.create_optimised_grid(18))
        )
        self.assertEqual(
            (232, 251, 12),
            self.module.get_best_square(self.module.create_optimised_grid(42))
        )

    def test_solver(self):
        self.assertEqual("90,269,16", self.module.solve(18))
        self.assertEqual("232,251,12", self.module.solve(42))


if __name__ == '__main__':
    unittest.main()
