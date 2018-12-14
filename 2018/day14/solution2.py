#!/usr/bin/env python
# -*- coding: utf-8 -*-


def update_elf_pos(recipes, pos):
    increment_by = recipes[pos] + 1
    pos += increment_by
    pos %= len(recipes)
    return pos


def make_hot_chocolate(recipes, elf1, elf2):
    new_recipe_total = recipes[elf1] + recipes[elf2]
    if new_recipe_total > 9:
        recipes.append(new_recipe_total // 10)
    recipes.append(new_recipe_total % 10)
    elf1 = update_elf_pos(recipes, elf1)
    elf2 = update_elf_pos(recipes, elf2)
    return (recipes, elf1, elf2)


def solve(input_value):
    input_value = [int(val) for val in input_value]
    recipes = [3, 7]
    elf1 = 0
    elf2 = 1

    length1 = len(input_value)
    length2 = len(input_value) + 1

    while input_value not in (recipes[-length1:], recipes[-length2: -1]):
        recipes, elf1, elf2 = make_hot_chocolate(recipes, elf1, elf2)

    if recipes[-length1:] == input_value:
        return len(recipes) - length1
    else:
        return len(recipes) - length2


if __name__ == '__main__':
    from timeit import default_timer as timer

    start = timer()

    solution = solve("540391")
    print(solution)

    end = timer()
    print()
    print("-" * 80)
    print("Time elapsed: {:.3f}s".format(end - start))
