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
