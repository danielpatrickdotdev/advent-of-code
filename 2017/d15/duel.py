#!/usr/bin/env python3


def get_input(path):
    with open(path) as infile:
        text = infile.read()

    a = text.split('\n')[0].split()[-1]
    b = text.split('\n')[1].split()[-1]
    return int(a), int(b)


a_mult = 16807
b_mult = 48271


def generator_x(mult, divisor, x):
    def generator(x):
        while True:
            x_product = mult * x
            x = x_product % divisor
            yield x
    return generator(x)


def generator_a(a):
    return generator_x(16807, 2147483647, a)


def generator_b(b):
    while True:
        b_product = b_mult * b
        b = b_product % 2147483647
        yield b


def generator_x2(gen, divisor):
    def generator():
        while True:
            x = next(gen)
            if x % divisor == 0:
                yield x
    return generator()


def generator_a2(a):
    return generator_x2(generator_a(a), 4)


def generator_b2(b):
    return generator_x2(generator_b(b), 8)


def count_matching_pairs(gen_a, gen_b, num_duels):
    count = 0

    for n in range(num_duels):
        a = next(gen_a)
        b = next(gen_b)
        if '{:032b}'.format(a)[-16:] == '{:032b}'.format(b)[-16:]:
            count += 1

    return count


if __name__ == '__main__':
    a, b = get_input("input.txt")
    gen_a = generator_a(a)
    gen_b = generator_b(b)
    print(count_matching_pairs(gen_a, gen_b, 40000000))

    gen_a = generator_a2(a)
    gen_b = generator_b2(b)
    print(count_matching_pairs(gen_a, gen_b, 5000000))
