#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pathlib import Path

from .common import remove_triggered_pairs


def solve(input_text):
    old_text = input_text

    while True:
        new_text = remove_triggered_pairs(old_text)
        if new_text == old_text:
            break

        old_text = new_text

    return len(new_text)


if __name__ == '__main__':
    from shared.utils import get_input

    input_path = Path(__file__).parent.joinpath("input.txt")
    input_text = get_input(input_path)[0]
    solution = solve(input_text)
    print(solution)
