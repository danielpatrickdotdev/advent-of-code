#!/usr/bin/env python3


def get_input(path):
    with open(path) as infile:
        return {int(d): int(r) for (d, r) in
            [line.rstrip('\n').split(':') for line in infile]
        }


class Scanner:

    def __init__(self, scan_range):
        self.range = scan_range


class Firewall:

    def __init__(self, data):
        self.firewall_size = max(data.keys()) + 1
        self.scanner_ranges = []

        for layer_number in range(self.firewall_size):
            if layer_number in data:
                self.scanner_ranges.append(data[layer_number])
            else:
                self.scanner_ranges.append(None)

    def get_catch_severity(self, pos):
        scanner_range = self.scanner_ranges[pos]
        if scanner_range is None:
            return 0
        else:
            return scanner_range * pos

    def get_trip_severity(self):
        return sum(map(self.get_catch_severity, self.get_trip_catches()))

    def get_trip_catches(self, delay=0):
        catches = []
        for n in range(self.firewall_size):
            scanner_range = self.scanner_ranges[n]
            if scanner_range is not None and \
                    (delay + n) % (2 * (scanner_range - 1)) == 0:
                catches.append(n)
        return catches

    def find_zero_severity_delay(self):
        for delay in range(1000000000):
            caught = False
            for n in range(self.firewall_size):
                if self.scanner_ranges[n] is not None and \
                        (delay + n) % (2 * (self.scanner_ranges[n] - 1)) == 0:
                    caught = True
                    break
            if not caught:
                return delay

        return None


if __name__ == '__main__':
    firewall_data = get_input("input.txt")
    f = Firewall(firewall_data)
    print("Severity:", f.get_trip_severity())
    delay = f.find_zero_severity_delay()
    if delay is not None:
        print("Delay by", delay, "picoseconds")
    else:
        print("It just won't work")
