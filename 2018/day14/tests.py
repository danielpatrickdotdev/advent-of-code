#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest

from . import solution1, solution2


class TestSolution1(unittest.TestCase):
    module = solution1

    def test_solver(self):
        self.assertEqual("5158916779", self.module.solve(9))
        self.assertEqual("0124515891", self.module.solve(5))
        self.assertEqual("9251071085", self.module.solve(18))
        self.assertEqual("5941429882", self.module.solve(2018))


class TestSolution2(unittest.TestCase):
    module = solution2
    expected = "lorem ipsum?"

    def test_solver(self):
        self.assertEqual(self.expected, self.module.solve("lorem ipsum"))


if __name__ == '__main__':
    unittest.main()
