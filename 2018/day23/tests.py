#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pathlib import Path
import unittest

from shared.utils import get_input
from . import solution1, solution2
from .nanobots import Nanobot, parse_nanobot


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


class TestNanobot(unittest.TestCase):
    def test_constructor(self):
        bot = Nanobot(0, 1, 2, 3)
        self.assertEqual(0, bot.x)
        self.assertEqual(1, bot.y)
        self.assertEqual(2, bot.z)
        self.assertEqual(3, bot.r)

    def test_range_property(self):
        bot = Nanobot(0, 1, 2, 3)
        self.assertEqual(3, bot.range)

    def test_pos_property(self):
        bot = Nanobot(0, 1, 2, 3)
        self.assertEqual((0, 1, 2), bot.pos)

    def test_in_range(self):
        bot1 = Nanobot(0, 1, 2, 3)
        bot2 = Nanobot(1, 2, 3, 4)
        bot3 = Nanobot(0, 0, 0, 0)

        self.assertTrue(bot1.in_range(0, 1, 2))
        self.assertTrue(bot1.in_range(1, 2, 3))
        self.assertTrue(bot1.in_range(0, 0, 0))
        self.assertFalse(bot1.in_range(0, 0, -1))

        self.assertTrue(bot2.in_range(1, 0, 1))
        self.assertFalse(bot2.in_range(0, 0, 1))

        self.assertTrue(bot3.in_range(0, 0, 0))
        self.assertFalse(bot3.in_range(-1, 0, 0))

    def test_parser(self):
        bot = parse_nanobot("pos=<0,0,0>, r=0")
        self.assertEqual((0, 0, 0), bot.pos)
        self.assertEqual(0, bot.range)

        bot = parse_nanobot("pos=<11,22,33>, r=10")
        self.assertEqual((11, 22, 33), bot.pos)
        self.assertEqual(10, bot.range)

        bot = parse_nanobot("pos=<-13,-22,-31>, r=100")
        self.assertEqual((-13, -22, -31), bot.pos)
        self.assertEqual(100, bot.range)


class TestSolution1(TestSolution):
    module = solution1
    expected = 7

    def test_solver(self):
        solution = self.module.solve(self.input_text)
        self.assertEqual(self.expected, solution)


class TestSolution2(TestSolution):
    module = solution2
    expected = "lorem ipsum?"

    def test_solver(self):
        solution = self.module.solve(self.input_text)
        self.assertEqual(self.expected, solution)


if __name__ == '__main__':
    unittest.main()
