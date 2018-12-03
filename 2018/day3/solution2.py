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

    return (num, result)


def combine_claims(claims_list):
    combined_claims = Counter()

    for claim in claims_list:
        for area in claim[1]:
            combined_claims[area] += 1

    return combined_claims


def check_for_overlaps(claim_areas, combined_claims):
    return any(combined_claims[area] > 1 for area in claim_areas)


def solve(input_text):
    claims = [parse_claim(line) for line in input_text]
    combined = combine_claims(claims)
    for claim in claims:
        if check_for_overlaps(claim[1], combined):
            continue
        else:
            return claim[0]


if __name__ == '__main__':
    from shared.utils import get_input

    input_path = Path(__file__).parent.joinpath("input.txt")
    input_text = get_input(input_path)
    solution = solve(input_text)
    print(solution)
