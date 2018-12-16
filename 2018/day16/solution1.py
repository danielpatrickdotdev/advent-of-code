#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pathlib import Path


def parse(input_text):
    instructions = []
    current_instruction = []
    last_line = None

    for line in input_text:
        if not line:
            if not last_line:
                break
            else:
                instructions.append(current_instruction)
                current_instruction = []

        elif line.split()[0] in ["Before:", "After:"]:
            current_instruction.append([
                int(c) for c in line[9: -1].split(", ")
            ])
        else:
            current_instruction.append([int(c) for c in line.split()])

        last_line = line

    return instructions


def solve(input_text):
    return " ".join(input_text) + "!"


if __name__ == '__main__':
    from shared.utils import get_input
    from timeit import default_timer as timer

    start = timer()

    input_path = Path(__file__).parent.joinpath("input.txt")
    input_text = get_input(input_path)
    solution = solve(input_text)
    print(solution)

    end = timer()
    print()
    print("-" * 80)
    print("Time elapsed: {:.3f}s".format(end - start))
