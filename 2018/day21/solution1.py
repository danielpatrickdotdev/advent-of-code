#!/usr/bin/env python
# -*- coding: utf-8 -*-


def solve():
    one = two = three = five = 0

    five = 65_536
    two = 2_238_642

    end = False
    while not end:
        three = five & 255
        two += three
        two &= 16_777_215
        two *= 65_899
        two &= 16_777_215

        if 256 > five:
            break

        three = 0

        while five >= 256:
            one = three + 1
            one *= 256
            if one > five:
                five = three
                break
            three += 1

    return two


if __name__ == '__main__':
    from timeit import default_timer as timer

    start = timer()

    solution = solve()
    print(solution)

    end = timer()
    print()
    print("-" * 80)
    print("Time elapsed: {:.3f}s".format(end - start))
