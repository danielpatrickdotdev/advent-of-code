#!/usr/bin/env python3

from functools import reduce


def get_input(path):
    with open(path) as infile:
        return infile.read()


def get_number_list(text):
    if text:
        return [int(n) for n in text.split(',')]
    else:
        return []


def convert_input_to_bytes(text):
    return [ord(c) for c in text] + [17, 31, 73, 47, 23]


class KnotHasher:

    def __init__(self, lengths, string_size):
        self.string_size = string_size
        self.starting_lengths = lengths.copy()

        self.reset()


    def reset(self):
        self.lengths = self.starting_lengths
        self.string = list(range(self.string_size))
        self.string_position = 0
        self.skip_size = 0


    def reverse(self, start, length):
        while length > 1:
            end = (start + length - 1) % len(self.string)
            start_char = self.string[start]
            end_char = self.string[end]
            self.string[start] = end_char
            self.string[end] = start_char
            start += 1
            start = start % len(self.string)
            length -= 2

    @property
    def lengths_position(self):
        return self.skip_size % len(self.lengths)

    def advance(self):
        self.string_position += self.lengths[self.lengths_position]
        self.string_position += self.skip_size # skip
        self.string_position = self.string_position % len(self.string)
        self.skip_size += 1

    def sparse_hash(self):
        for length in self.lengths:
            self.reverse(self.string_position, length)
            self.advance()

    def hex(self, num):
        return '{:02x}'.format(num)

    def dense_hash(self):
        result = ""
        generator = (i for i in self.string)
        for n in range(16):
            elements = list(next(generator) for n in range(16))
            sixteenth = reduce(lambda i, j: i ^ j, elements)
            result += self.hex(sixteenth)
        return result

    def hash(self, rounds=1, dense=False):
        for round in range(rounds):
            self.sparse_hash()

        if dense:
            result = self.dense_hash()
        else:
            result = self.string
        self.reset()
        return result


if __name__ == '__main__':
    STRING_SIZE = 256
    input_text = get_input("input.txt")
    number_list = get_number_list(input_text)

    knothash = KnotHasher(number_list, STRING_SIZE)
    hashed = knothash.hash()
    print(hashed[:10])
    print("Answer:", hashed[0] * hashed[1])

    byte_list = convert_input_to_bytes(input_text)
    knothash = KnotHasher(byte_list, STRING_SIZE)
    print(knothash.hash(64, True))
