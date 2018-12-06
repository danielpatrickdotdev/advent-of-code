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
        self.input_text = get_input(self.input_path)


class CoordsMixin:
    test_coords = [
        (1, 1),
        (1, 6),
        (8, 3),
        (3, 4),
        (5, 5),
        (8, 9),
    ]


class TestCommon(unittest.TestCase, CoordsMixin):
    module = common
    test_input = [
        "1, 1",
        "1, 6",
        "8, 3",
        "3, 4",
        "5, 5",
        "8, 9",
    ]

    def test_parse(self):
        self.assertEqual(self.test_coords, self.module.parse(self.test_input))

    def test_get_max_x_and_y(self):
        x, y = self.module.get_max_x_and_y(self.test_coords)
        self.assertEqual(8, x)
        self.assertEqual(9, y)

    def test_get_manhattan_distance(self):
        values_to_test = [
            (0, 0, (1, 1), 2),
            (5, 0, (1, 1), 5),
            (5, 0, (5, 5), 5),
            (1, 1, (1, 1), 0),
        ]
        for x, y, coord, expected in values_to_test:
            self.assertEqual(
                expected, self.module.get_manhattan_distance(x, y, coord)
            )

    def test_complete_grid(self):
        expected = [
            [None, None, None, None, None, None, None, None, None, None],
            [None, 0, None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None, 2, None],
            [None, None, None, 3, None, None, None, None, None, None],
            [None, None, None, None, None, 4, None, None, None, None],
            [None, 1, None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None, 5, None],
            [None, None, None, None, None, None, None, None, None, None],
        ]

        def some_pointless_func(x, y, coords):
            if (x, y) in coords:
                return coords.index((x, y))
            else:
                return None

        grid = self.module.complete_grid(self.test_coords, some_pointless_func)
        self.assertEqual(expected, grid)


class TestSolution1(TestSolution, CoordsMixin):
    module = solution1
    expected = 17

    def test_get_closest_destination(self):
        values_to_test = [
            (0, 0, 0),
            (5, 0, None),
            (5, 1, None),
            (5, 2, 4),
            (1, 1, 0),
        ]
        for x, y, expected in values_to_test:
            self.assertEqual(
                expected,
                self.module.get_closest_destination(x, y, self.test_coords)
            )

    def test_complete_grid_with_get_closest_destination(self):
        expected = [
            [0, 0, 0, 0, 0, None, 2, 2, 2, 2],
            [0, 0, 0, 0, 0, None, 2, 2, 2, 2],
            [0, 0, 0, 3, 3, 4, 2, 2, 2, 2],
            [0, 0, 3, 3, 3, 4, 2, 2, 2, 2],
            [None, None, 3, 3, 3, 4, 4, 2, 2, 2],
            [1, 1, None, 3, 4, 4, 4, 4, 2, 2],
            [1, 1, 1, None, 4, 4, 4, 4, None, None],
            [1, 1, 1, None, 4, 4, 4, 5, 5, 5],
            [1, 1, 1, None, 4, 4, 5, 5, 5, 5],
            [1, 1, 1, None, 5, 5, 5, 5, 5, 5],
            [1, 1, 1, None, 5, 5, 5, 5, 5, 5],
        ]
        grid = common.complete_grid(self.test_coords,
                                    self.module.get_closest_destination)
        self.assertEqual(expected, grid)


    def test_solver(self):
        solution = self.module.solve(self.input_text)
        self.assertEqual(self.expected, solution)


class TestSolution2(TestSolution, CoordsMixin):
    module = solution2
    expected = 16

    def test_calculate_distance_from_all_coords(self):
        result = self.module.calculate_distance_from_all_coords(
            4, 3, self.test_coords)
        self.assertEqual(30, result)

    def test_solver(self):
        solution = self.module.solve(self.input_text)
        self.assertEqual(self.expected, solution)


if __name__ == '__main__':
    unittest.main()
