#!/usr/bin/env python
# -*- coding: utf-8 -*-


from collections import defaultdict
import re

regex = re.compile(
    "position=<([- ]?\d+), ([- ]?\d+)> velocity=<([- ]?\d+), ([- ]?\d+)>"
)

def parse(input_text):
    result = []

    for line in input_text:
        x, y, dx, dy = regex.match(line).groups()
        result.append([(int(x), int(y)), (int(dx), int(dy))])

    return result
