#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pathlib import Path
import unittest

from shared.utils import get_input
from . import solution1, solution2, common
from .rescue import RescueMessage


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


class TestValues:
    test_inputs = [
        "position=< 9,  1> velocity=< 0,  2>",
        "position=< 7,  0> velocity=<-1,  0>",
        "position=< 3, -2> velocity=<-1,  1>",
        "position=< 6, 10> velocity=<-2, -1>",
        "position=< 2, -4> velocity=< 2,  2>",
        "position=<-6, 10> velocity=< 2, -2>",
        "position=< 1,  8> velocity=< 1, -1>",
        "position=< 1,  7> velocity=< 1,  0>",
        "position=<-3, 11> velocity=< 1, -2>",
        "position=< 7,  6> velocity=<-1, -1>",
        "position=<-2,  3> velocity=< 1,  0>",
        "position=<-4,  3> velocity=< 2,  0>",
        "position=<10, -3> velocity=<-1,  1>",
        "position=< 5, 11> velocity=< 1, -2>",
        "position=< 4,  7> velocity=< 0, -1>",
        "position=< 8, -2> velocity=< 0,  1>",
        "position=<15,  0> velocity=<-2,  0>",
        "position=< 1,  6> velocity=< 1,  0>",
        "position=< 8,  9> velocity=< 0, -1>",
        "position=< 3,  3> velocity=<-1,  1>",
        "position=< 0,  5> velocity=< 0, -1>",
        "position=<-2,  2> velocity=< 2,  0>",
        "position=< 5, -2> velocity=< 1,  2>",
        "position=< 1,  4> velocity=< 2,  1>",
        "position=<-2,  7> velocity=< 2, -2>",
        "position=< 3,  6> velocity=<-1, -1>",
        "position=< 5,  0> velocity=< 1,  0>",
        "position=<-6,  0> velocity=< 2,  0>",
        "position=< 5,  9> velocity=< 1, -2>",
        "position=<14,  7> velocity=<-2,  0>",
        "position=<-3,  6> velocity=< 2, -1>",
    ]
    parser_outputs = [
        [(9, 1), (0, 2)],
        [(7, 0), (-1, 0)],
        [(3, -2), (-1, 1)],
        [(6, 10), (-2, -1)],
        [(2, -4), (2, 2)],
        [(-6, 10), (2, -2)],
        [(1, 8), (1, -1)],
        [(1, 7), (1, 0)],
        [(-3, 11), (1, -2)],
        [(7, 6), (-1, -1)],
        [(-2, 3), (1, 0)],
        [(-4, 3), (2, 0)],
        [(10, -3), (-1, 1)],
        [(5, 11), (1, -2)],
        [(4, 7), (0, -1)],
        [(8, -2), (0, 1)],
        [(15, 0), (-2, 0)],
        [(1, 6), (1, 0)],
        [(8, 9), (0, -1)],
        [(3, 3), (-1, 1)],
        [(0, 5), (0, -1)],
        [(-2, 2), (2, 0)],
        [(5, -2), (1, 2)],
        [(1, 4), (2, 1)],
        [(-2, 7), (2, -2)],
        [(3, 6), (-1, -1)],
        [(5, 0), (1, 0)],
        [(-6, 0), (2, 0)],
        [(5, 9), (1, -2)],
        [(14, 7), (-2, 0)],
        [(-3, 6), (2, -1)],
    ]
    zero_seconds = [
        "........#.............",
        "................#.....",
        ".........#.#..#.......",
        "......................",
        "#..........#.#.......#",
        "...............#......",
        "....#.................",
        "..#.#....#............",
        ".......#..............",
        "......#...............",
        "...#...#.#...#........",
        "....#..#..#.........#.",
        ".......#..............",
        "...........#..#.......",
        "#...........#.........",
        "...#.......#..........",
    ]
    one_second = [
        "......................",
        "......................",
        "..........#....#......",
        "........#.....#.......",
        "..#.........#......#..",
        "......................",
        "......#...............",
        "....##.........#......",
        "......#.#.............",
        ".....##.##..#.........",
        "........#.#...........",
        "........#...#.....#...",
        "..#...........#.......",
        "....#.....#.#.........",
        "......................",
        "......................",
    ]
    two_seconds = [
        "......................",
        "......................",
        "......................",
        "..............#.......",
        "....#..#...####..#....",
        "......................",
        "........#....#........",
        "......#.#.............",
        ".......#...#..........",
        ".......#..#..#.#......",
        "....#....#.#..........",
        ".....#...#...##.#.....",
        "........#.............",
        "......................",
        "......................",
        "......................",
    ]
    three_seconds = [
        "......................",
        "......................",
        "......................",
        "......................",
        "......#...#..###......",
        "......#...#...#.......",
        "......#...#...#.......",
        "......#####...#.......",
        "......#...#...#.......",
        "......#...#...#.......",
        "......#...#...#.......",
        "......#...#..###......",
        "......................",
        "......................",
        "......................",
        "......................",
    ]
    four_seconds = [
        "......................",
        "......................",
        "......................",
        "............#.........",
        "........##...#.#......",
        "......#.....#..#......",
        ".....#..##.##.#.......",
        ".......##.#....#......",
        "...........#....#.....",
        "..............#.......",
        "....#......#...#......",
        ".....#.....##.........",
        "...............#......",
        "...............#......",
        "......................",
        "......................",
    ]


class TestRescueMessage(unittest.TestCase, TestValues):
    def test_constructor(self):
        rm = RescueMessage(self.parser_outputs)
        self.assertEqual("\n".join(self.zero_seconds), str(rm))


class TestCommon(unittest.TestCase, TestValues):
    module = common

    def test_parser(self):
        self.assertEqual(
            self.parser_outputs,
            self.module.parse(self.test_inputs)
        )


class TestSolution1(TestSolution):
    module = solution1
    expected = [
        "#...#..###",
        "#...#...#.",
        "#...#...#.",
        "#####...#.",
        "#...#...#.",
        "#...#...#.",
        "#...#...#.",
        "#...#..###",
    ]

    def test_solver(self):
        solution = self.module.solve(self.input_text)
        self.assertEqual("\n".join(self.expected), solution)


class TestSolution2(TestSolution):
    module = solution2
    expected = 3

    def test_solver(self):
        solution = self.module.solve(self.input_text)
        self.assertEqual(self.expected, solution)


if __name__ == '__main__':
    unittest.main()
