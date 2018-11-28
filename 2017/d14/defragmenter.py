#!/usr/bin/env python3


from knothash import KnotHasher, convert_input_to_bytes


def get_input(path):
    with open(path) as infile:
        return infile.read()


class Disc:

    def __init__(self, data):
        self.rows = self.scan_disc(data)

    def scan_disc(self, puzzle_input):
        rows = []
        for n in range(128):
            byte_list = convert_input_to_bytes(puzzle_input + "-" + str(n))
            k = KnotHasher(byte_list, 256)
            khash = k.hash(64, True)

            row = ''.join(['{:04b}'.format(int(c, 16)) for c in khash])
            rows.append([int(c) for c in row])

        return rows

    def get_used_squares(self):
        return sum([sum(row) for row in self.rows])

    def get_adjacent_used_squares(self, x, y):
        adj = []
        if not x == 0:
            adj.append((x - 1, y))
        if not x == 127:
            adj.append((x + 1, y))
        if not y == 0:
            adj.append((x, y - 1))
        if not y == 127:
            adj.append((x, y + 1))

        adj = filter(lambda xy: self.rows[xy[1]][xy[0]] == 1, adj)
        return adj

    def remove_adjacent_used_squares(self, x, y):
        to_remove = [(x, y)]
        while to_remove:
            x, y = to_remove.pop()
            self.rows[y][x] = -1
            to_remove += self.get_adjacent_used_squares(x, y)

    def count_groups(self):
        groups = 0
        for x in range(128):
            for y in range(128):
                if self.rows[y][x] == 1:
                    groups += 1
                    self.remove_adjacent_used_squares(x, y)
        return groups


if __name__ == '__main__':
    puzzle_input = get_input("input.txt")
    disc = Disc(puzzle_input)
    print("Used squares:", disc.get_used_squares())
    print("Number of groups:", disc.count_groups())
