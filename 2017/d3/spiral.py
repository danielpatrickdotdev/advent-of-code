#!/usr/bin/env python3

from math import sqrt
import sys

num = int(sys.argv[1])

def distance(n):
    if n == 1:
        return 0
    ring = round(sqrt(n-1) // 1 / 2 + 0.0000001)
    length = ring * 2 + 1
    return ring + abs(length // 2 - ((n - (length - 2) ** 2) % (length - 1)))


print(distance(num))
