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


def old_react_polymer(text):
    while True:
        new_text = remove_triggered_pairs(text)
        if new_text == text:
            break

        text = new_text

    return new_text


def react_polymer(text):
    text = list(text)
    result = []
    i = 0

    while i < len(text):
        if not result:
            # result is empty
            result.append(text[i])
        elif check_trigger(result[-1], text[i]):
            # Compare last item added to result with next item in text.
            # If it triggers a reaction, remove last char from result - when we
            # advance i, we effectively skip these two characters
            result.pop()
        else:
            # tentatively add char to result - could still be removed later on
            result.append(text[i])

        i += 1

    return "".join(result)
