#!/usr/bin/env python3

def import_input(path):
    with open(path, encoding='utf-8') as infile:
        return [int(n) for n in infile.read().split()]


banks = import_input("input.txt")


class Redistributor:
    def __init__(self, banks):
        self._banks = banks

    def redistribute(self, i):
        blocks = self._banks[i]
        self._banks[i] = 0

        while blocks > 0:
            i += 1
            i = i % len(self._banks)

            self._banks[i] += 1
            blocks -= 1

    def find_biggest_bank(self):
        return self._banks.index(max(self._banks))

    def solve(self):
        count = 0

        records = []

        while self._banks not in records:
            records.append(self._banks.copy())

            i = self.find_biggest_bank()
            self.redistribute(i)
            count += 1

        return count

    def solve2(self):
        count = 0
        target = self._banks.copy()
        current = None

        while current != target:
            i = self.find_biggest_bank()
            self.redistribute(i)
            count += 1
            current = self._banks.copy()

        return count

r = Redistributor(banks)
print(r.solve())
print(r.solve2())
