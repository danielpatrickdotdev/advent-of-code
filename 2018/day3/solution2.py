#!/usr/bin/env python
# -*- coding: utf-8 -*-

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

    return (num, result)


def do_claims_overlap(claim1, claim2):
    for area in claim1:
        if any([area == a for a in claim2]):
            return True

    return False


def has_overlaps(claim, other_claims):
    for other_claim in other_claims:
        if do_claims_overlap(claim[1], other_claim[1]):
            return True

    return False


def solve(input_text):
    return " ".join(input_text) + "?"


if __name__ == '__main__':
    from shared.utils import get_input

    input_path = Path(__file__).parent.joinpath("input.txt")
    input_text = get_input(input_path)
    solution = solve(input_text)
    print(solution)
