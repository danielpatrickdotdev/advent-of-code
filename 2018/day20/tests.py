#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pathlib import Path
import unittest

from shared.utils import get_input
from . import solution1, solution2
from .facility import FacilityMap


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


class DataForTests:
    test_input1 = "^WNE$"
    test_input2 = "^ENWWW(NEEE|SSE(EE|N))$"
    test_input3 = "^ENNWSWW(NEWS|)SSSEEN(WNSE|)EE(SWEN|)NNN$"
    test_input4 = "^ESSWWN(E|NNENN(EESS(WNSE|)SSS|WWWSSSSE(SW|NNNE)))$"
    test_input5 = (
        "^WSSEESWWWNW(S|NENNEEEENN(ESSSSW(NWSW|SSEN)"
        "|WSWWN(E|WWS(E|SS))))$"
    )
    test_instructions1 = ["W", "N", "E"]
    test_instructions2 = [
        "E", "N", "W", "W", "W",
        ["N", "E", "E", "E", "|", "S", "S", "E", ["E", "E", "|", "N"]]
    ]
    test_instructions3 = [
        "E", "N", "N", "W", "S", "W", "W",
        ["N", "E", "W", "S", "|"], "S", "S", "S", "E", "E", "N",
        ["W", "N", "S", "E", "|"], "E", "E",
        ["S", "W", "E", "N", "|"], "N", "N", "N",
    ]
    test_map1 = (
        "#####\n"
        "#.|.#\n"
        "#—###\n"
        "#.|X#\n"
        "#####"
    )
    test_map2 = (
        "#########\n"
        "#.|.|.|.#\n"
        "#—#######\n"
        "#.|.|.|.#\n"
        "#—#####—#\n"
        "#.#.#X|.#\n"
        "#—#—#####\n"
        "#.|.|.|.#\n"
        "#########"
    )
    test_map3 = (
        "###########\n"
        "#.|.#.|.#.#\n"
        "#—###—#—#—#\n"
        "#.|.|.#.#.#\n"
        "#—#####—#—#\n"
        "#.#.#X|.#.#\n"
        "#—#—#####—#\n"
        "#.#.|.|.|.#\n"
        "#—###—###—#\n"
        "#.|.|.#.|.#\n"
        "###########"
    )
    test_map4 = (
        "#############\n"
        "#.|.|.|.|.|.#\n"
        "#—#####—###—#\n"
        "#.#.|.#.#.#.#\n"
        "#—#—###—#—#—#\n"
        "#.#.#.|.#.|.#\n"
        "#—#—#—#####—#\n"
        "#.#.#.#X|.#.#\n"
        "#—#—#—###—#—#\n"
        "#.|.#.|.#.#.#\n"
        "###—#—###—#—#\n"
        "#.|.#.|.|.#.#\n"
        "#############"
    )
    test_map5 = (
        "###############\n"
        "#.|.|.|.#.|.|.#\n"
        "#—###—###—#—#—#\n"
        "#.|.#.|.|.#.#.#\n"
        "#—#########—#—#\n"
        "#.#.|.|.|.|.#.#\n"
        "#—#—#########—#\n"
        "#.#.#.|X#.|.#.#\n"
        "###—#—###—#—#—#\n"
        "#.|.#.#.|.#.|.#\n"
        "#—###—#####—###\n"
        "#.|.#.|.|.#.#.#\n"
        "#—#—#####—#—#—#\n"
        "#.#.|.|.|.#.|.#\n"
        "###############"
    )


class TestFacilityMap(unittest.TestCase, DataForTests):
    def test_parse(self):
        self.assertEqual(
            self.test_instructions1, FacilityMap().parse(self.test_input1)
        )
        self.assertEqual(
            self.test_instructions2, FacilityMap().parse(self.test_input2)
        )
        self.assertEqual(
            self.test_instructions3, FacilityMap().parse(self.test_input3)
        )

    def test_create_tree1(self):
        facility = FacilityMap()
        facility.instructions = self.test_instructions1
        facility.create_tree()
        facility.create_grid()
        self.assertEqual(self.test_map1, str(facility))

    def test_create_tree2(self):
        facility = FacilityMap()
        facility.instructions = self.test_instructions2
        facility.create_tree()
        facility.create_grid()
        self.assertEqual(self.test_map2, str(facility))

    def test_create_tree3(self):
        facility = FacilityMap()
        facility.instructions = self.test_instructions3
        facility.create_tree()
        facility.create_grid()
        self.assertEqual(self.test_map3, str(facility))

    def test_constructor(self):
        self.assertEqual(self.test_map1, str(FacilityMap(self.test_input1)))
        self.assertEqual(self.test_map2, str(FacilityMap(self.test_input2)))
        self.assertEqual(self.test_map3, str(FacilityMap(self.test_input3)))
        self.assertEqual(self.test_map4, str(FacilityMap(self.test_input4)))
        self.assertEqual(self.test_map5, str(FacilityMap(self.test_input5)))

    def test_get_farthest_room(self):
        self.assertEqual(3, FacilityMap(self.test_input1).get_farthest_room())
        self.assertEqual(10, FacilityMap(self.test_input2).get_farthest_room())
        self.assertEqual(18, FacilityMap(self.test_input3).get_farthest_room())
        self.assertEqual(23, FacilityMap(self.test_input4).get_farthest_room())
        self.assertEqual(31, FacilityMap(self.test_input5).get_farthest_room())


class TestSolution1(TestSolution, DataForTests):
    module = solution1
    expected = 31

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
