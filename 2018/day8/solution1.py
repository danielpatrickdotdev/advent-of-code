#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pathlib import Path

from .common import parse
from .tree import Tree


def sum_nodes(node):
    if not node.children:
        return sum(node.meta)
    else:
        return sum(
            sum_nodes(child) for child in node.children
        ) + sum(node.meta)


def solve(input_text):
    tree = Tree(parse(input_text))
    return sum_nodes(tree)


if __name__ == '__main__':
    from shared.utils import get_input

    input_path = Path(__file__).parent.joinpath("input.txt")
    input_text = get_input(input_path)
    solution = solve(input_text)
    print(solution)
