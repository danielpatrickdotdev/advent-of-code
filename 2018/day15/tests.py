#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pathlib import Path
import unittest

from shared.utils import get_input
from . import solution1, solution2
from .caves import Caves, ElfOrGoblin


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


class TestElfOrGoblin(unittest.TestCase):
    def test_constructor(self):
        goblin = ElfOrGoblin(0, 1)
        self.assertEqual(0, goblin.x)
        self.assertEqual(1, goblin.y)
        self.assertEqual(200, goblin.hit_points)
        self.assertEqual(3, goblin.attack_power)
        self.assertFalse(goblin.is_dead)

    def test_move(self):
        goblin = ElfOrGoblin(0, 1)
        goblin.move(4, 5)
        self.assertEqual(4, goblin.x)
        self.assertEqual(5, goblin.y)

    def test_damage(self):
        goblin = ElfOrGoblin(0, 1)
        goblin.hit_points = 1
        goblin.damage(3)

        self.assertEqual(0, goblin.hit_points)
        self.assertTrue(goblin.is_dead)

    def test_attack(self):
        goblin = ElfOrGoblin(0, 1)
        elf = ElfOrGoblin(1, 1)
        goblin.attack(goblin)
        self.assertEqual(197, goblin.hit_points)
        self.assertFalse(goblin.is_dead)

        elf.hit_points = 3
        goblin.attack(elf)
        self.assertEqual(0, elf.hit_points)
        self.assertTrue(elf.is_dead)

        elf2 = ElfOrGoblin(1,1)
        elf2.attack_power = 2
        elf2.attack(goblin)
        self.assertEqual(195, goblin.hit_points)
        self.assertFalse(goblin.is_dead)

        goblin.hit_points = 1
        elf2.attack(goblin)
        self.assertEqual(0, goblin.hit_points)
        self.assertTrue(goblin.is_dead)


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
