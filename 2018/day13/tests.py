#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pathlib import Path
import unittest

from shared.utils import get_input
from . import solution1, solution2, common
from .tracks import Tracks
from .cart import Cart


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
    initial_data = [
        ["/",  "-", ">",  "-", "\\", " ", " ", " ",  " ", " ",  " ", " ", " "],
        ["|",  " ", " ",  " ", "|",  " ", " ", "/",  "-", "-",  "-", "-", "\\"],
        ["|",  " ", "/",  "-", "+",  "-", "-", "+",  "-", "\\", " ", " ", "|"],
        ["|",  " ", "|",  " ", "|",  " ", " ", "|",  " ", "v",  " ", " ", "|"],
        ["\\", "-", "+",  "-", "/",  " ", " ", "\\", "-", "+",  "-", "-", "/"],
        [" ",  " ", "\\", "-", "-",  "-", "-", "-",  "-", "/",  " ", " ", " "],
    ]
    initial_tracks = [
        ["/",  "-", "-",  "-", "\\", " ", " ", " ",  " ", " ",  " ", " ", " "],
        ["|",  " ", " ",  " ", "|",  " ", " ", "/",  "-", "-",  "-", "-", "\\"],
        ["|",  " ", "/",  "-", "+",  "-", "-", "+",  "-", "\\", " ", " ", "|"],
        ["|",  " ", "|",  " ", "|",  " ", " ", "|",  " ", "|",  " ", " ", "|"],
        ["\\", "-", "+",  "-", "/",  " ", " ", "\\", "-", "+",  "-", "-", "/"],
        [" ",  " ", "\\", "-", "-",  "-", "-", "-",  "-", "/",  " ", " ", " "],
    ]


class TestCart(unittest.TestCase, TestValues):
    def test_move(self):
        expected_strings = [
            "3, 0, >", "4, 0, v", "4, 1, v", "4, 2, >", "5, 2, >",
            "6, 2, >", "7, 2, >", "8, 2, >", "9, 2, v", "9, 3, v",
            "9, 4, <", "8, 4, <", "7, 4, ^", "7, 3, ^", "7, 2, <",
        ]

        cart = Cart(2, 0, ">")
        tracks = Tracks(self.initial_tracks)

        for expected in expected_strings:
            cart.move(tracks)
            self.assertEqual(expected, str(cart))

        cart.crashed = True
        cart.move(tracks)
        self.assertEqual(expected_strings[-1], str(cart))

    def test_move2(self):
        expected_strings = [
            "9, 4, >",
            "10, 4, >",
            "11, 4, >",
            "12, 4, ^",
        ]

        cart = Cart(9, 3, "v")
        tracks = Tracks(self.initial_tracks)

        for expected in expected_strings:
            cart.move(tracks)
            self.assertEqual(expected, str(cart))

    def test_move3(self):
        initial_tracks = [
            ["/",  "\\", " ",  " "],
            ["+",  "+",  "+",  "+"],
            [" ",  " ",  "\\", "/"],
        ]
        tracks = Tracks(initial_tracks)
        cart = Cart(0, 0, "v")
        expected_strings = [
            "0, 1, >",
            "1, 1, >",
            "2, 1, v",
            "2, 2, >",
            "3, 2, ^",
            "3, 1, <",
            "2, 1, <",
            "1, 1, ^",
            "1, 0, <",
            "0, 0, v",
        ]
        for expected in expected_strings:
            cart.move(tracks)
            self.assertEqual(expected, str(cart))


class TestTracks(unittest.TestCase, TestValues):
    input_filename = "test_input.txt"

    def test_get(self):
        tracks = Tracks(self.initial_tracks)
        self.assertEqual("-", tracks.get(1, 0))


class TestCommon(unittest.TestCase, TestValues):
    module = common

    def test_get_missing_track(self):
        to_test = [
            ([[" ", "|", " "], ["-", "<", "-"], [" ", "|", " "]], "+"),
            ([[" ", "\\", " "], ["-", "<", "-"], [" ", "\\", " "]], "+"),
            ([[" ", "\\", " "], ["-", "<", "-"], [" ", "|", " "]], "+"),
            ([[" ", "\\", " "], ["-", "<", "-"], [" ", "/", " "]], "+"),
            ([[" ", "/", " "], ["-", "<", "-"], [" ", "/", " "]], "+"),
            ([[" ", "|", " "], ["-", "<", "-"], [" ", "/", " "]], "+"),
            ([[" ", "/", " "], ["-", "<", "-"], [" ", "|", " "]], "+"),
            ([[" ", " ", " "], ["-", "<", "-"], [" ", " ", " "]], "-"),
            ([["-", "-", "-"], ["-", "<", "-"], ["-", "-", "-"]], "-"),
            ([[" ", " ", " "], ["\\", "<", "-"], [" ", " ", " "]], "-"),
            ([[" ", " ", " "], ["/", "<", "-"], [" ", " ", " "]], "-"),
            ([[" ", " ", " "], ["/", "<", "\\"], [" ", " ", " "]], "-"),
            ([[" ", " ", " "], ["-", "<", "\\"], [" ", " ", " "]], "-"),
            ([[" ", " ", " "], ["\\", "<", "\\"], [" ", " ", " "]], "-"),
            ([[" ", " ", " "], ["\\", "<", "/"], [" ", " ", " "]], "-"),
            ([[" ", " ", " "], ["-", "<", "/"], [" ", " ", " "]], "-"),
            ([[" ", " ", " "], ["/", "<", "/"], [" ", " ", " "]], "-"),
            ([[" ", "|", " "], [" ", "^", " "], [" ", "|", " "]], "|"),
            ([[" ", "|", "|"], ["\\", "^", "|"], ["|", "|", "|"]], "|"),
            ([[" ", "|", " "], [" ", "^", " "], [" ", "/", " "]], "|"),
            ([[" ", "/", " "], [" ", "^", " "], [" ", "|", " "]], "|"),
            ([[" ", "/", " "], [" ", "^", " "], [" ", "/", " "]], "|"),
            ([[" ", "/", " "], [" ", "^", " "], [" ", "\\", " "]], "|"),
            ([[" ", "\\", " "], [" ", "^", " "], [" ", "/", " "]], "|"),
            ([[" ", "\\", " "], [" ", "^", " "], [" ", "|", " "]], "|"),
            ([[" ", "\\", " "], [" ", "^", " "], [" ", "\\", " "]], "|"),
            ([[" ", "|", " "], [" ", "^", " "], [" ", "\\", " "]], "|"),
        ]
        for data, expected in to_test:
            self.assertEqual(
                expected, self.module.get_missing_track(data, 1, 1)
            )

    def test_parser(self):
        tracks, carts = self.module.parse(self.initial_data)
        self.assertEqual(self.initial_tracks, tracks.data)
        self.assertEqual(2, len(carts))
        self.assertCountEqual(
            ["2, 0, >", "9, 3, v"],
            [str(cart) for cart in carts]
        )

    def test_move_carts(self):
        tracks = Tracks(self.initial_tracks)
        carts = [Cart(0, 0, ">"), Cart(4, 0, "<")]
        self.module.move_carts(carts, tracks)

        self.assertEqual("1, 0, >", str(carts[0]))
        self.assertFalse(carts[0].has_crashed())
        self.assertEqual("3, 0, <", str(carts[1]))
        self.assertFalse(carts[1].has_crashed())

        self.module.move_carts(carts, tracks)

        self.assertEqual("2, 0, >", str(carts[0]))
        self.assertTrue(carts[0].has_crashed())
        self.assertEqual("2, 0, <", str(carts[1]))
        self.assertTrue(carts[1].has_crashed())

    def test_move_carts2(self):
        track_arg = [
            "/""-""-""-""\\"" "" ",
            "|"" "" "" ""|"" "" ",
            "|"" ""/""-""+""-""\\",
            "|"" ""|"" ""|"" ""|",
            "\\""-""+""-""/"" ""|",
            " "" ""|"" "" "" ""|",
            " "" ""\\""-""-""-""/",
        ]
        tracks = Tracks(track_arg)
        carts = [Cart(1, 4, ">"), Cart(3, 4, "<")]
        self.module.move_carts(carts, tracks)
        self.assertEqual("2, 4, ^", str(carts[0]))
        self.assertTrue(carts[0].has_crashed())
        self.assertEqual("2, 4, v", str(carts[1]))
        self.assertTrue(carts[1].has_crashed())


class TestSolution1(TestSolution):
    module = solution1
    expected = "7,3"

    def test_solver(self):
        solution = self.module.solve(self.input_text)
        self.assertEqual(self.expected, solution)


class TestSolution2(TestSolution):
    module = solution2
    input_filename = "test_input2.txt"
    expected = "6,4"

    def test_solver(self):
        solution = self.module.solve(self.input_text)
        self.assertEqual(self.expected, solution)


if __name__ == '__main__':
    unittest.main()
