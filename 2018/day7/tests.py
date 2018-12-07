#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pathlib import Path
import unittest

from shared.utils import get_input
from . import solution1, solution2, common
from .worker import Worker


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


class TestCommon(unittest.TestCase):
    module = common
    test_input = [
        "Step C must be finished before step A can begin.",
        "Step C must be finished before step F can begin.",
        "Step A must be finished before step B can begin.",
        "Step A must be finished before step D can begin.",
        "Step B must be finished before step E can begin.",
        "Step D must be finished before step E can begin.",
        "Step F must be finished before step E can begin.",
    ]
    requirements_dict = {
        "C": ["A", "F"],
        "A": ["B", "D"],
        "B": ["E"],
        "D": ["E"],
        "F": ["E"],
    }

    def test_parser(self):
        self.assertEqual(self.requirements_dict,
                         self.module.parse(self.test_input))

    def test_get_steps(self):
        self.assertEqual(set("ABCDEF"),
                         self.module.get_steps(self.requirements_dict))

    def test_get_available(self):
        self.assertEqual(
            set("C"),
            self.module.get_available(self.requirements_dict, set("ABCDEF"))
        )


class TestSolution1(TestSolution):
    module = solution1
    expected = "CABDFE"

    def test_solver(self):
        solution = self.module.solve(self.input_text)
        self.assertEqual(self.expected, solution)


class TestWorker(unittest.TestCase):
    def test_construct_worker(self):
        worker1 = Worker()
        self.assertTrue(worker1.is_idle())
        self.assertIsNone(worker1.current_job)
        self.assertIsNone(worker1.last_job)

    def test_work_on(self):
        worker1 = Worker()
        worker1.work_on("A", 1)
        self.assertFalse(worker1.is_idle())
        self.assertEqual("A", worker1.current_job)

    def test_work_on_when_busy(self):
        worker1 = Worker()
        worker1.work_on("A", 1)

        with self.assertRaises(Exception):
            worker1.work_on("B", 2)

    def test_work(self):
        worker1 = Worker()
        worker1.work_on("A", 1)
        self.assertFalse(worker1.is_idle())

        worker1.work()
        self.assertTrue(worker1.is_idle())
        self.assertIsNone(worker1.current_job)
        self.assertEqual("A", worker1.last_job)

    def test_last_job(self):
        worker1 = Worker()
        worker1.work_on("A", 1)
        self.assertIsNone(worker1.last_job)

        worker1.work()
        self.assertEqual("A", worker1.last_job)


class TestSolution2(TestSolution):
    module = solution2
    expected = 15

    def test_increment_workers(self):
        workers = [Worker(), Worker()]
        workers[0].work_on("A", 1)
        workers[1].work_on("B", 2)

        self.module.increment_workers(workers)

        self.assertTrue(workers[0].is_idle())
        self.assertFalse(workers[1].is_idle())

        self.module.increment_workers(workers)

        self.assertTrue(workers[0].is_idle())
        self.assertTrue(workers[1].is_idle())

    def test_solver(self):
        solution = self.module.solve(self.input_text)
        self.assertEqual(self.expected, solution)


if __name__ == '__main__':
    unittest.main()
