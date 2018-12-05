#!/usr/bin/env python
# -*- coding: utf-8 -*-

def check_trigger(one, two):
    return one.lower() == two.lower() and one != two


def remove_triggered_pairs(text):
    n = 0
    while n < (len(text) - 1):
        if check_trigger(text[n], text[n + 1]):
            text = text[:n] + text[n + 2:]
        else:
            n += 1

    return text
