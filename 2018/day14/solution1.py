#!/usr/bin/env python
# -*- coding: utf-8 -*-


def solve(input_value):
    return "{}".format(input_value)


if __name__ == '__main__':
    from timeit import default_timer as timer

    start = timer()

    solution = solve(540391)
    print(solution)

    end = timer()
    print()
    print("-" * 80)
    print("Time elapsed: {:.3f}s".format(end - start))
