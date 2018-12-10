#!/usr/bin/env python
# -*- coding: utf-8 -*-

from collections import Counter
from pathlib import Path
import re


claim_regex = re.compile("^#(\d+) @ (\d+),(\d+): (\d+)x(\d+)$")


def parse_claim(claim_string):
    match = claim_regex.match(claim_string)
    groups = match.groups()
    num, x, y, dx, dy = [int(group) for group in groups]

    result = []
    for i in range(x, x + dx):
        for j in range(y, y + dy):
            result.append((i, j))

    return result


def combine_claims(claims_list):
    combined_claims = Counter()

    for claim in claims_list:
        for area in claim:
            combined_claims[area] += 1

    return combined_claims


def solve(input_text):
    claims = [parse_claim(line) for line in input_text]
    combined = combine_claims(claims)
    return sum([n > 1 for n in combined.values()])


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
    print("Time elapsed: {:.3f}".format(end - start))
