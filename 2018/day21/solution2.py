#!/usr/bin/env python
# -*- coding: utf-8 -*-


def solve():
    one = two = three = five = 0
    last_new_two = None
    twos_found = set()

    while True:
        five = two | 65_536
        two = 2_238_642

        while True:
            three = five & 255
            two += three
            two &= 16_777_215
            two *= 65_899
            two &= 16_777_215

            if 256 > five:
                if two in twos_found:
                    return last_new_two
                else:
                    last_new_two = two
                    twos_found.add(two)

                break

            three = 0
            while five >= 256:
                one = three + 1
                one *= 256
                if one > five:
                    five = three
                    break
                three += 1


if __name__ == '__main__':
    from timeit import default_timer as timer

    start = timer()

    solution = solve()
    print(solution)

    end = timer()
    print()
    print("-" * 80)
    print("Time elapsed: {:.3f}s".format(end - start))
