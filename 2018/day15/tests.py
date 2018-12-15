#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pathlib import Path
import unittest

from shared.utils import get_input
from . import solution1, solution2
from .caves import Caves, CombatantBaseClass, Elf, Goblin


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


class Orc(CombatantBaseClass):
    letter = "O"


class Pixie(CombatantBaseClass):
    letter = "P"


class TestCombatantBaseClass(unittest.TestCase):

    def test_constructor(self):
        pixie = Pixie(0, 1)
        self.assertEqual(0, pixie.x)
        self.assertEqual(1, pixie.y)
        self.assertEqual(200, pixie.hit_points)
        self.assertEqual(3, pixie.attack_power)
        self.assertFalse(pixie.is_dead)

    def test_move(self):
        pixie = Pixie(0, 1)
        pixie.move(4, 5)
        self.assertEqual(4, pixie.x)
        self.assertEqual(5, pixie.y)

    def test_damage(self):
        pixie = Pixie(0, 1)
        pixie.hit_points = 1
        pixie.damage(3)

        self.assertEqual(0, pixie.hit_points)
        self.assertTrue(pixie.is_dead)

    def test_attack(sorc):
        orc = Orc(1, 1)
        pixie = Pixie(0, 1)
        pixie.attack(pixie)
        sorc.assertEqual(197, pixie.hit_points)
        sorc.assertFalse(pixie.is_dead)

        orc.hit_points = 3
        pixie.attack(orc)
        sorc.assertEqual(0, orc.hit_points)
        sorc.assertTrue(orc.is_dead)

        orc2 = Orc(1, 1)
        orc2.attack_power = 2
        orc2.attack(pixie)
        sorc.assertEqual(195, pixie.hit_points)
        sorc.assertFalse(pixie.is_dead)

        pixie.hit_points = 1
        orc2.attack(pixie)
        sorc.assertEqual(0, pixie.hit_points)
        sorc.assertTrue(pixie.is_dead)

    def test_str(self):
        orc = Orc(1, 1)
        self.assertEqual("O", str(orc))

        pixie = Pixie(0, 1)
        self.assertEqual("P", str(pixie))


class TestElf(unittest.TestCase):
    def test_str(self):
        elf = Elf(1, 1)
        self.assertEqual("E", str(elf))


class TestGoblin(unittest.TestCase):
    def test_str(self):
        goblin = Goblin(0, 1)
        self.assertEqual("G", str(goblin))


class TestCaves(unittest.TestCase):
    example_input1 = [
        "#########",
        "#G..G..G#",
        "#.......#",
        "#.......#",
        "#G..E..G#",
        "#.......#",
        "#.......#",
        "#G..G..G#",
        "#########",
    ]
    example_cave1 = [
        ["#", "#", "#", "#", "#", "#", "#", "#", "#"],
        ["#", "G", ".", ".", "G", ".", ".", "G", "#"],
        ["#", ".", ".", ".", ".", ".", ".", ".", "#"],
        ["#", ".", ".", ".", ".", ".", ".", ".", "#"],
        ["#", "G", ".", ".", "E", ".", ".", "G", "#"],
        ["#", ".", ".", ".", ".", ".", ".", ".", "#"],
        ["#", ".", ".", ".", ".", ".", ".", ".", "#"],
        ["#", "G", ".", ".", "G", ".", ".", "G", "#"],
        ["#", "#", "#", "#", "#", "#", "#", "#", "#"],
    ]
    example_elves1 = [(4, 4)]
    example_goblins1 = [
        (1, 1), (4, 1), (7, 1), (1, 4), (7, 4), (1, 7), (4, 7), (7, 7)
    ]

    def test_constructor(self):
        caves = Caves(self.example_input1)
        self.assertEqual(self.example_cave1, caves.grid)
        self.assertEqual(self.example_elves1, caves.elves)
        self.assertEqual(self.example_goblins1, caves.goblins)


class TestSolution1(TestSolution):
    module = solution1
    expected = 27730

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
