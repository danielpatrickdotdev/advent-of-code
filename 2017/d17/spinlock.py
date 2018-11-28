#!/usr/bin/env python3

import sys



class Spinlock:

    def __init__(self, times, step_size):
        self.buffer = [0]
        self.pos = 0
        self.next_number = 1
        self.step_size = step_size
        self.times = times

    def spin(self):
        while self.next_number <= self.times:
            self.step()

    def add_cyles(self, n):
        self.times += n

    def step(self):
        self.pos += self.step_size
        self.pos %= len(self.buffer)
        self.pos += 1
        self.buffer.insert(self.pos, self.next_number)
        self.next_number += 1

    @property
    def after_last_value(self):
        pos = (self.pos + 1) % len(self.buffer)
        return self.buffer[pos]

    def print(self, n):
        return ' '.join(
            [str(i) for i in self.buffer[self.pos - n:self.pos + n + 1]]
        )

    @property
    def value_after_zero(self):
        zero_pos = self.buffer.index(0)
        answer_pos = (zero_pos + 1) % len(self.buffer)
        return self.buffer[answer_pos]

    def __repr__(self):
        return ' '.join([str(i) for i in self.buffer])


def spinlock2(times, step_size):
    last_after_zero = None
    pos = 0
    length = 1
    for n in range(times):
        pos += step_size
        pos %= length
        pos += 1
        length += 1
        if pos == 1:
            last_after_zero = n + 1
    return last_after_zero


if __name__ == '__main__':
    step_size = int(sys.argv[1])
    spinlock = Spinlock(2017, step_size)
    spinlock.spin()
    #print(spinlock)
    print(spinlock.after_last_value)
    print(spinlock.print(3))
    after_zero = spinlock2(50000000, step_size)
    print(after_zero)
