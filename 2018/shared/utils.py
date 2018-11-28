#!/usr/bin/env python
# -*- coding: utf-8 -*-


def get_input(path):
    with open(path) as infile:
        return [line.rstrip('\n') for line in infile]
