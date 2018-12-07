#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pathlib import Path
import re


regex = re.compile(
    "^Step ([A-Z]) must be finished before step ([A-Z]) can begin.$")


def parse(input_text):
    requirements = {}
    for line in input_text:
        char1, char2 = regex.match(line).groups()
        if char1 in requirements:
            requirements[char1].append(char2)
        else:
            requirements[char1] = [char2]

    return requirements


def get_steps(requirements):
    result = set(requirements.keys())
    result.update(v for values in requirements.values() for v in values)
    return result


def get_available(requirements_not_satisfied, steps_remaining):
    not_available = [
        item for items in requirements_not_satisfied.values() for item in items
    ]
    return steps_remaining - set(not_available)
