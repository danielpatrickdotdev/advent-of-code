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

    def test_get_location(self):
        pixie = Pixie(0, 1)
        self.assertEqual((0, 1), pixie.get_location())

        pixie.move(1, 1)
        self.assertEqual((1, 1), pixie.get_location())

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

    def test_attack(self):
        orc = Orc(1, 1)
        pixie = Pixie(0, 1)
        pixie.attack(pixie)
        self.assertEqual(197, pixie.hit_points)
        self.assertFalse(pixie.is_dead)

        orc.hit_points = 3
        pixie.attack(orc)
        self.assertEqual(0, orc.hit_points)
        self.assertTrue(orc.is_dead)

        orc2 = Orc(1, 1)
        orc2.attack_power = 2
        orc2.attack(pixie)
        self.assertEqual(195, pixie.hit_points)
        self.assertFalse(pixie.is_dead)

        pixie.hit_points = 1
        orc2.attack(pixie)
        self.assertEqual(0, pixie.hit_points)
        self.assertTrue(pixie.is_dead)

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
    example_input2 = [
        "#######",
        "#.G...#",
        "#...EG#",
        "#.#.#G#",
        "#..G#E#",
        "#.....#",
        "#######",
    ]
    example_input3 = [
        "#######",
        "#..G..#",
        "#...EG#",
        "#.#G#G#",
        "#...#E#",
        "#.....#",
        "#######",
    ]
    example_cave1 = (
        "#########\n"
        "#G..G..G#\n"
        "#.......#\n"
        "#.......#\n"
        "#G..E..G#\n"
        "#.......#\n"
        "#.......#\n"
        "#G..G..G#\n"
        "#########"
    )
    example_cave1_after_three_moves = (
        "#########\n"
        "#.......#\n"
        "#..GGG..#\n"
        "#..GEG..#\n"
        "#G..G...#\n"
        "#......G#\n"
        "#.......#\n"
        "#.......#\n"
        "#########"
    )
    example_elf1 = (4, 4)
    example_goblins1 = [
        (1, 1), (4, 1), (7, 1), (1, 4), (7, 4), (1, 7), (4, 7), (7, 7)
    ]

    def test_constructor(self):
        caves = Caves(self.example_input1)
        self.assertEqual(self.example_cave1, str(caves))
        self.assertEqual(1, len(caves.elves))
        self.assertEqual(self.example_elf1, caves.elves[0].get_location())
        self.assertEqual(8, len(caves.goblins))
        for n, coords in enumerate(self.example_goblins1):
            self.assertEqual(coords, caves.goblins[n].get_location())

    def test_in_range(self):
        caves = Caves(self.example_input1)
        elf = Elf(1, 1)
        in_range = [(1, 0), (0, 1), (2, 1), (1, 2)]

        for x, y in in_range:
            self.assertTrue(caves.in_range(elf, Goblin(x, y)))

        not_in_range = [(0, 0), (2, 0), (0, 2), (2, 2), (3, 1), (1, 3)]

        for x, y in not_in_range:
            self.assertFalse(caves.in_range(elf, Goblin(x, y)))

    def test_get_best_move(self):
        caves = Caves(self.example_input1)

        self.assertEqual(
            (2, 1), caves.get_best_move(caves.grid[1][1], caves.elves)
        )

    def test_get_best_move2(self):
        caves = Caves(self.example_input3)

        self.assertEqual(
            (4, 1), caves.get_best_move(caves.grid[3][1], caves.elves)
        )

    def test_get_best_move3(self):
        test_input = [
            "########",
            "#.E....#",
            "#......#",
            "#....G.#",
            "#...G..#",
            "#G.....#",
            "########",
        ]
        caves = Caves(test_input)
        self.assertEqual(
            (3, 1), caves.get_best_move(caves.grid[2][1], caves.goblins)
        )

    def test_get_best_move4(self):
        test_input = [
            "######",
            "#.G..#",
            "##..##",
            "#...E#",
            "#E...#",
            "######",
        ]
        caves = Caves(test_input)
        self.assertEqual(
            (2, 2), caves.get_best_move(caves.grid[2][1], caves.elves)
        )

    def test_advance(self):
        goblin_moves = [
            [(2, 1), (6, 1), (4, 2), (7, 3), (2, 4), (1, 6), (4, 6), (7, 6)],
            [(3, 1), (5, 1), (4, 2), (2, 3), (6, 3), (1, 5), (4, 5), (7, 5)],
            [(3, 2), (4, 2), (5, 2), (3, 3), (5, 3), (1, 4), (4, 4), (7, 5)],
        ]
        elf_moves = [
            [(4, 3)], [(4, 3)], [(4, 3)],
        ]
        caves = Caves(self.example_input1)

        for n in range(len(goblin_moves)):
            caves.advance()
            self.assertEqual(
                elf_moves[n], [e.get_location() for e in caves.elves]
            )
            self.assertEqual(
                goblin_moves[n], [g.get_location() for g in caves.goblins]
            )

    def test_get_opponents_within_range(self):
        arg = self.example_cave1_after_three_moves.split("\n")
        caves = Caves(arg)
        elf = caves.grid[4][3]
        caves.grid[5][3].hit_points = 199
        expected_goblins = [
            caves.grid[5][3], caves.grid[4][2],
            caves.grid[3][3], caves.grid[4][4],
        ]
        self.assertEqual(
            expected_goblins, caves.get_opponents_within_range(elf)
        )

    def test_advance_attack_result(self):
        arg = self.example_cave1_after_three_moves.split("\n")
        caves = Caves(arg)
        caves.grid[4][2].hit_points = 199
        caves.advance()

        self.assertEqual(200, caves.goblins[0].hit_points)
        self.assertEqual(196, caves.goblins[1].hit_points)
        self.assertEqual(200, caves.goblins[2].hit_points)
        self.assertEqual(200, caves.goblins[3].hit_points)
        self.assertEqual(200, caves.goblins[4].hit_points)
        self.assertEqual(200, caves.goblins[5].hit_points)
        self.assertEqual(200, caves.goblins[6].hit_points)
        self.assertEqual(200, caves.goblins[7].hit_points)
        self.assertEqual(188, caves.elves[0].hit_points)


class TestSolution1(TestSolution):
    module = solution1
    expected = 27730
    start_two = [
        "#######",
        "#G..#E#",
        "#E#E.E#",
        "#G.##.#",
        "#...#E#",
        "#...E.#",
        "#######",
    ]
    start_three = [
        "#######",
        "#E..EG#",
        "#.#G.E#",
        "#E.##E#",
        "#G..#.#",
        "#..E#.#",
        "#######",
    ]
    start_four = [
        "#######",
        "#E.G#.#",
        "#.#G..#",
        "#G.#.G#",
        "#G..#.#",
        "#...E.#",
        "#######",
    ]
    start_five = [
        "#######",
        "#.E...#",
        "#.#..G#",
        "#.###.#",
        "#E#G#G#",
        "#...#G#",
        "#######",
    ]

    start_six = [
        "#########",
        "#G......#",
        "#.E.#...#",
        "#..##..G#",
        "#...##..#",
        "#...#...#",
        "#.G...G.#",
        "#.....G.#",
        "#########",
    ]

    def test_solver(self):
        solution = self.module.solve(self.input_text)
        self.assertEqual(self.expected, solution)

    def test_solver2(self):
        solution = self.module.solve(self.start_two)
        self.assertEqual(36334, solution)

    def test_solver3(self):
        solution = self.module.solve(self.start_three)
        self.assertEqual(39514, solution)

    def test_solver4(self):
        solution = self.module.solve(self.start_four)
        self.assertEqual(27755, solution)

    def test_solver5(self):
        solution = self.module.solve(self.start_five)
        self.assertEqual(28944, solution)

    def test_solver6(self):
        solution = self.module.solve(self.start_six)
        self.assertEqual(18740, solution)


class TestSolution2(TestSolution):
    module = solution2
    expected = 4988
    input_text2 = [
        "#######",
        "#E..EG#",
        "#.#G.E#",
        "#E.##E#",
        "#G..#.#",
        "#..E#.#",
        "#######",
    ]
    expected2 = 31284
    input_text3 = [
        "#######",
        "#E.G#.#",
        "#.#G..#",
        "#G.#.G#",
        "#G..#.#",
        "#...E.#",
        "#######",
    ]
    expected3 = 3478
    input_text4 = [
        "#######",
        "#.E...#",
        "#.#..G#",
        "#.###.#",
        "#E#G#G#",
        "#...#G#",
        "#######",
    ]
    expected4 = 6474
    input_text5 = [
        "#########",
        "#G......#",
        "#.E.#...#",
        "#..##..G#",
        "#...##..#",
        "#...#...#",
        "#.G...G.#",
        "#.....G.#",
        "#########",
    ]
    expected5 = 1140

    def test_solver(self):
        solution = self.module.solve(self.input_text)
        self.assertEqual(self.expected, solution)

    def test_solver2(self):
        solution = self.module.solve(self.input_text2)
        self.assertEqual(self.expected2, solution)

    def test_solver3(self):
        solution = self.module.solve(self.input_text3)
        self.assertEqual(self.expected3, solution)

    def test_solver4(self):
        solution = self.module.solve(self.input_text4)
        self.assertEqual(self.expected4, solution)

    def test_solver5(self):
        solution = self.module.solve(self.input_text5)
        self.assertEqual(self.expected5, solution)


if __name__ == '__main__':
    unittest.main()
