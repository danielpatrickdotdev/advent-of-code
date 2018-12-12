#!/usr/bin/env python
# -*- coding: utf-8 -*-


def parse(input_text):
    plant_state = input_text.pop(0).split()[-1]
    input_text.pop(0)

    rules = []

    for rule in input_text:
        pattern, _, result = rule.split()
        if result == "#":
            rules.append(pattern)

    return plant_state, rules
