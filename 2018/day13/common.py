#!/usr/bin/env python
# -*- coding: utf-8 -*-

from operator import attrgetter

from .tracks import Tracks
from .cart import Cart


def get_missing_track(data, x, y):
    height = len(data)
    width = len(data[0])

    # assuming no carts start next to each other!
    up = data[y - 1][x] if y > 0 else None
    down = data[y + 1][x] if (y + 1) < height else None
    left = data[y][x - 1] if x > 0 else None
    right = data[y][x + 1] if (x + 1) < width else None

    vertical = ["|", "+", "\\", "/"]
    horizontal = ["-", "+", "\\", "/"]

    if up in vertical:
        if down in vertical:
            if left in horizontal and right in horizontal:
                return "+"
            else:
                return "|"
        elif left in horizontal:
            return "/"
        elif right in horizontal:
            return "\\"
    elif down in vertical:
        if left in horizontal:
            return "/"
        elif right in horizontal:
            return "\\"
    elif left in horizontal and right in horizontal:
        return "-"

    # should probably raise an error if we get to here and new_char == None
    return None


def parse(input_text):
    carts = []
    tracks_arg = []

    for y in range(len(input_text)):
        row = []
        tracks_arg.append(row)

        for x in range(len(input_text[y])):
            char = input_text[y][x]
            if char in "^>v<":
                carts.append(Cart(x, y, char))
                row.append(get_missing_track(input_text, x, y))
            else:
                row.append(char)

    return Tracks(tracks_arg), carts


def move_carts(carts, tracks):
    carts.sort(key=attrgetter("y", "x"))

    for cart in carts:
        if not cart.has_crashed():
            cart.move(tracks)

            for other_cart in carts:
                if other_cart.has_crashed() or other_cart is cart:
                    continue
                elif other_cart.x == cart.x and other_cart.y == cart.y:
                    other_cart.set_crashed()
                    cart.set_crashed()
                    break
