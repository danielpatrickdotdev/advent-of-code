#!/usr/bin/env python3

import sys


captcha = sys.argv[2]

def puzzle_one(captcha):
    result = 0
    for n in range(len(captcha)):
        a = captcha[n]
        b = captcha[n+1] if len(captcha) > (n + 1) else captcha[0]

        if a == b:
            result += int(a)
    return result

def puzzle_two(captcha):
    length = len(captcha)
    half = int(length / 2)
    result = 0

    for n in range(length):
        a = captcha[n]
        b = captcha[(n + half) % length]

        if a == b:
            result += int(a)
    return result

if sys.argv[1] == "one":
    print(puzzle_one(captcha))
else:
    print(puzzle_two(captcha))
