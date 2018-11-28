#!/usr/bin/env python3

import unittest

from plumber import Plumber


class TestPlumber(unittest.TestCase):

    def test_init(self):
        pipes = [
            "1 <-> 1",
            "2 <-> 3, 4, 5"
        ]
        p = Plumber(pipes)
        self.assertEqual({1:[1], 2:[3,4,5]}, p.pipes)

    def test_count_network(self):
        pipes = [
            "1 <-> 1",
            "2 <-> 3, 4, 5",
            "3 <-> 2",
            "4 <-> 2, 5",
            "5 <-> 2, 4, 6",
            "6 <-> 5"
        ]
        plumber = Plumber(pipes)
        self.assertEqual(1, plumber.count_network(1))
        self.assertEqual(5, plumber.count_network(2))
        self.assertEqual(5, plumber.count_network(3))
        self.assertEqual(5, plumber.count_network(4))
        self.assertEqual(5, plumber.count_network(5))
        self.assertEqual(5, plumber.count_network(6))


if __name__ == '__main__':
    unittest.main()
