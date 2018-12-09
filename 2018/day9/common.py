#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re


regex = re.compile(
    "^(\d+) players; last marble is worth (\d+) points$")


def parse(input_text):
    return tuple(int(match) for match in regex.match(input_text[0]).groups())
