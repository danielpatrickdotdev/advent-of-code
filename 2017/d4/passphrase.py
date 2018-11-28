#!/usr/bin/env python3

from operator import eq as isequal

def import_passphrases(path):
    with open(path, encoding='utf-8') as infile:
        return [line for line in infile]


passphrases = import_passphrases("passphrases.txt")


def check_passphrase(func, passphrase):
    valid = True
    words = []

    for word in passphrase.split():
        if any(map(lambda w: func(word, w), words)):
            valid = False
            break
        else:
            words.append(word)

    return valid

def isanagram(p1, p2):
    return set(p1) == set(p2)


print("test1:", sum(map(lambda p: check_passphrase(isequal, p), passphrases)))
print("test2:", sum(map(lambda p: check_passphrase(isanagram, p), passphrases)))
