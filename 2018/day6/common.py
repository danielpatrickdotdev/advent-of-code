#!/usr/bin/env python
# -*- coding: utf-8 -*-


def parse(input_text):
    return [(int(x), int(y)) for x, y in (line.split(", ") for line in input_text)]
