#!/usr/bin/env python3

import sys


def import_spreadsheet(path):
    with open(path, encoding='utf-8') as infile:
        spreadsheet = [
            [int(n) for n in line.split()] for line in infile
        ]
    return spreadsheet

spreadsheet = import_spreadsheet("spreadsheet.txt")
print(sum([max(row) - min(row) for row in spreadsheet]))

def find_divisible_and_divide(numbers):
    for i in range(len(numbers)):
        for j in range(len(numbers)):
            if i != j and (numbers[i] % numbers[j] == 0):
                return numbers[i] // numbers[j]


print(sum([find_divisible_and_divide(row) for row in spreadsheet]))
