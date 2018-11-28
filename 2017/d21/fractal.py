#!/usr/bin/env python3

import sys


def get_input(path):
    with open(path) as infile:
        return [line for line in infile.read().split('\n')]


class Rule:

    def __init__(self, text):
        i, o = text.split('=>')
        self.input_patterns = self.create_input_patterns(i)
        self.output_pattern = self.create_output_pattern(o)

    def __eq__(self, other):
        return tuple(other) in self.input_patterns

    @property
    def output(self):
        return self.output_pattern[:]

    def rotate90(self, pattern):
        l = len(pattern)
        r = range(l)
        return tuple([''.join([pattern[l - j - 1][i] for j in r]) for i in r])

    def create_input_patterns(self, pattern):
        pattern = tuple([row.strip() for row in pattern.split('/')])
        patterns = [pattern]

        rot90 = self.rotate90(pattern)
        patterns.append(rot90)

        rot180 = self.rotate90(rot90)
        patterns.append(rot180)

        rot270 = self.rotate90(rot180)
        patterns.append(rot270)

        h_flipped = [self.h_flip(p) for p in patterns]
        v_flipped = [self.v_flip(p) for p in patterns]
        return set(patterns + h_flipped + v_flipped)

    def h_flip(self, pattern):
        return tuple([row[::-1] for row in pattern])

    def v_flip(self, pattern):
        return tuple(reversed(pattern))

    def create_output_pattern(self, pattern):
        return tuple([row.strip() for row in pattern.split('/')])

    def printable_pattern(self, pattern):
        return '\n'.join([row for row in pattern])


class ArtEnhancer:

    def __init__(self, rules_text, original_art):
        self.original_art = original_art
        self.modified_art = original_art.split('/')
        self.rules = []
        for rule_text in rules_text:
            self.rules.append(Rule(rule_text))

    def enhance(self, num_times):
        for n in range(num_times):
            self._enhance()

    def _enhance(self):
        height = len(self.modified_art)
        if height % 2 == 0:
            step = 2
        else:
            step = 3

        new_art = []
        matched = True

        for i in range(0, height, step):
            rows = ["" for n in range(step + 1)]

            for j in range(0, height, step):
                to_translate = [
                    r[j:j + step] for r in self.modified_art[i:i + step]
                ]
                matched_rule = None

                for rule in self.rules:
                    if rule == to_translate:
                        matched_rule = rule
                        break

                if matched_rule is not None:
                    output = matched_rule.output
                    for n in range(step + 1):
                        rows_n = rows[n]
                        output_n = output[n]
                        rows[n] += output[n]
                else:
                    matched = False
                    for rule in self.rules:
                        for pattern in rule.input_patterns:
                            print(pattern, pattern == tuple(to_translate))
                            print(tuple(to_translate))
                        print()
            new_art += rows
        if matched:
            self.modified_art = new_art[:]
        else:
            raise Exception

    @property
    def art(self):
        return '/'.join(self.modified_art)

    def count_on_pixels(self):
        return sum([s.count('#') for s in self.modified_art])

    def __repr__(self):
        return '\n'.join(self.modified_art)


if __name__ == '__main__':
    n = int(sys.argv[1])
    art = ".#./..#/###"
    rules = get_input("input.txt")
    enhancer = ArtEnhancer(rules, art)
    enhancer.enhance(n)
    if n <= 8:
        print(enhancer)
    print("Number of 'on' pixels:", enhancer.count_on_pixels())
