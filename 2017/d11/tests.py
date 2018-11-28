#!/usr/bin/env python3

import unittest
from unittest import mock

from infinite import InfiniteGrid, get_input


class TestImportFile(unittest.TestCase):

    @mock.patch("builtins.open", create=True)
    def test_get_input(self, mock_open):
        mock_open.side_effect = [
            mock.mock_open(read_data="Data1").return_value,
            mock.mock_open(read_data="Data2").return_value
        ]

        self.assertEqual("Data1", get_input("fileA"))
        mock_open.assert_called_once_with("fileA")
        mock_open.reset_mock()

        self.assertEqual("Data2", get_input("fileB"))
        mock_open.assert_called_once_with("fileB")


class TestInfiniteGrid(unittest.TestCase):

    def test_get_route(self):
        strings_and_directions = {
            "":        [],
            "n": ["n"],
            "n,ne":   ["n", "ne"]
        }
        grid = InfiniteGrid()

        for string, route in strings_and_directions.items():
            self.assertEqual(route, grid.get_route(string))

    def test_simplify_directions(self):
        pass

    def test_simplify_opposites(self):
        inputs_and_outputs = [
            (["n", "nw", "nw"], ["n", "nw", "nw"]),
            (["ne", "n", "n", "s"], ["ne", "n"]),
            (["se", "n", "ne", "s"], ["se", "ne"]),
            (["s", "se", "se", "nw"], ["s", "se"]),
            (["se", "n", "s", "nw"], []),
            (["nw", "se", "sw", "ne", "n", "s"], [])
        ]
        grid = InfiniteGrid()

        for i, o in inputs_and_outputs:
            self.assertEqual(
                grid.simplify_opposites(grid.route_dict(i)),
                grid.route_dict(o)
            )

    def test_simplify_next_but_ones(self):
        inputs_and_outputs = [
            (["n", "nw", "nw", "ne"], ["n", "n", "nw"]),
            (["ne", "n", "n", "se"], ["ne", "ne", "n"]),
            (["se", "ne", "ne", "s"], ["se", "se", "ne"]),
            (["s", "se", "se", "sw"], ["s", "s", "se"]),
            (["sw", "s", "s", "nw"], ["sw", "sw", "s"]),
            (["nw", "sw", "sw", "n"], ["nw", "nw", "sw"])
        ]
        grid = InfiniteGrid()

        for i, o in inputs_and_outputs:
            self.assertEqual(
                grid.simplify_next_but_ones(grid.route_dict(i)),
                grid.route_dict(o)
            )

    def test_route_dict(self):
        expected = [
            ([], {"n": 0, "ne": 0, "se": 0, "s": 0, "sw": 0, "nw": 0}),
            (
                ["ne","ne","nw","s","ne","ne","ne","ne"],
                {"ne": 6, "nw": 1, "s": 1, "n": 0, "se": 0, "sw": 0}
            )
        ]
        grid = InfiniteGrid()

        for i, o in expected:
            self.assertEqual(o, grid.route_dict(i))

    def test_simplify(self):
        inputs_and_outputs = [
            (["ne","ne","ne"], ["ne", "ne", "ne"]),
            (["ne","ne","sw","sw"], []),
            (["ne","ne","s","s"], ["se", "se"]),
            (["se","sw","se","sw","sw"], ["s", "s", "sw"])
        ]
        grid = InfiniteGrid()

        for i, o in inputs_and_outputs:
            self.assertEqual(grid.route_dict(o), grid.simplify(i))

    def test_simplify_and_count(self):
        inputs_and_outputs = [
            (["ne","ne","ne"], 3),
            (["ne","ne","sw","sw"], 0),
            (["ne","ne","s","s"], 2),
            (["se","sw","se","sw","sw"], 3)
        ]
        grid = InfiniteGrid()

        for i, o in inputs_and_outputs:
            self.assertEqual(o, grid.simplify_and_count(i))

    def test_get_furthest_point_on_route(self):
        inputs_and_outputs = [
            (["ne","ne","ne"], 3),
            (["ne","ne","sw","sw"], 2),
            (["ne","ne","s","s"], 2),
            (["se","sw","se","sw","sw"], 3)
        ]
        grid = InfiniteGrid()

        for i, o in inputs_and_outputs:
            self.assertEqual(o, grid.get_furthest_point_on_route(i))


if __name__ == '__main__':
    unittest.main()
