#!/usr/bin/env python
# -*- coding: utf-8 -*-

from collections import deque
import re


regex = re.compile(
    "^(\d+) players; last marble is worth (\d+) points$")


def parse(input_text):
    return tuple(int(match) for match in regex.match(input_text[0]).groups())


def place_marble(circle, next_marble):
    circle.rotate(-1)
    circle.append(next_marble)


def play_game(num_players, num_marbles):
    players = [0 for n in range(num_players)]

    circle = deque([0])
    current_player = 0

    for n in range(1, num_marbles + 1):
        if n % 23 == 0:
            circle.rotate(7)
            players[current_player] += n
            players[current_player] += circle.pop()
            circle.rotate(-1)
        else:
            place_marble(circle, n)

        current_player += 1
        current_player %= num_players

    return players
