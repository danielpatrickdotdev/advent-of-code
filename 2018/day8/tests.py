#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pathlib import Path
import unittest

from shared.utils import get_input
from . import solution1, solution2, common
from .tree import Tree


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


class TestTree(unittest.TestCase):
    test_input = [2, 3, 0, 3, 10, 11, 12, 1, 1, 0, 1, 99, 2, 1, 1, 2]

    def test_len(self):
        tree = Tree(self.test_input, 9)
        self.assertEqual(3, len(tree))

        tree = Tree(self.test_input, 0)
        self.assertEqual(16, len(tree))

    def test_parse_node_with_leaf(self):
        self.assertEqual(
            ([], [99], 3),
            Tree.parse_node(None, self.test_input, 9)
        )

    def test_parse_node_with_root(self):
        children, metadata, length = Tree.parse_node(None, self.test_input, 0)
        self.assertEqual(2, len(children))
        self.assertEqual([1, 1, 2], metadata)
        self.assertEqual(16, length)

    def test_create_single_node_tree(self):
        tree = Tree(self.test_input, 9)
        self.assertEqual([], tree.children)
        self.assertEqual([99], tree.meta)

    def test_create_multi_node_tree(self):
        tree = Tree(self.test_input)
        self.assertEqual(2, len(tree.children))
        self.assertEqual([1, 1, 2], tree.meta)

        child1 = tree.children[0]
        self.assertEqual([], child1.children)
        self.assertEqual([10, 11, 12], child1.meta)

        child2 = tree.children[1]
        self.assertEqual(1, len(child2.children))
        self.assertEqual([2], child2.meta)

        grandchild = child2.children[0]
        self.assertEqual([], grandchild.children)
        self.assertEqual([99], grandchild.meta)


class TestCommon(unittest.TestCase):
    module = common
    test_input = ["2 3 0 3 10 11 12 1 1 0 1 99 2 1 1 2"]
    parsed_input = [2, 3, 0, 3, 10, 11, 12, 1, 1, 0, 1, 99, 2, 1, 1, 2]

    def test_parser(self):
        self.assertEqual(self.parsed_input, self.module.parse(self.test_input))


class TestSolution1(TestSolution):
    module = solution1
    expected = 138
    parsed_input = [2, 3, 0, 3, 10, 11, 12, 1, 1, 0, 1, 99, 2, 1, 1, 2]

    def test_sum_nodes(self):
        tree = Tree(self.parsed_input)
        node1 = tree.children[0]
        node2 = tree.children[1]
        node3 = tree.children[1].children[0]

        self.assertEqual(33, self.module.sum_nodes(node1))
        self.assertEqual(101, self.module.sum_nodes(node2))
        self.assertEqual(99, self.module.sum_nodes(node3))
        self.assertEqual(138, self.module.sum_nodes(tree))

    def test_solver(self):
        solution = self.module.solve(self.input_text)
        self.assertEqual(self.expected, solution)


class TestSolution2(TestSolution):
    module = solution2
    expected = 66
    parsed_input = [2, 3, 0, 3, 10, 11, 12, 1, 1, 0, 1, 99, 2, 1, 1, 2]

    def test_sum_nodes(self):
        tree = Tree(self.parsed_input)
        node1 = tree.children[0]
        node2 = tree.children[1]
        node3 = tree.children[1].children[0]

        self.assertEqual(33, self.module.sum_nodes(node1))
        self.assertEqual(0, self.module.sum_nodes(node2))
        self.assertEqual(99, self.module.sum_nodes(node3))
        self.assertEqual(66, self.module.sum_nodes(tree))

    def test_solver(self):
        solution = self.module.solve(self.input_text)
        self.assertEqual(self.expected, solution)


if __name__ == '__main__':
    unittest.main()
