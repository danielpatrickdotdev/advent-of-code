#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pathlib import Path


def get_unit_types(text):
    unit_types = set(char.upper() for char in text)

    return "".join(unit_types)


def remove_unit_type(unit_type, text):
    text = text.replace(unit_type, "")
    text = text.replace(unit_type.lower(), "")
    return text


def solve(input_text):
    return input_text + "?"


if __name__ == '__main__':
    from shared.utils import get_input

    input_path = Path(__file__).parent.joinpath("input.txt")
    input_text = get_input(input_path)[0]
    solution = solve(input_text)
    print(solution)
