#!/usr/bin/env python
# -*- coding: utf-8 -*-

from itertools import combinations
from pathlib import Path


def parser(input_text):
    return [line for line in input_text]


def count_differences(text1, text2):
    # assume lengths agree because they do for known inputs
        if len(text1) == 0:
            return 0
        else:
            match = 0 if text1[-1] == text2[-1] else 1
            return match + count_differences(text1[:-1], text2[:-1])


def find_off_by_one_pair(box_ids):
    id_pairs = combinations(box_ids, 2)
    for id1, id2 in id_pairs:
        if count_differences(id1, id2) == 1:
            return(id1, id2)


def get_matching_letters(text1, text2):
    # assume lengths agree because they do for known inputs
    if len(text1) == 0:
        return ""
    match = text1[-1] if text1[-1] == text2[-1] else ""
    return get_matching_letters(text1[:-1], text2[:-1]) + match


def solve(input_text):
    box_ids = parser(input_text)
    one, two = find_off_by_one_pair(box_ids)
    return get_matching_letters(one, two)


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
