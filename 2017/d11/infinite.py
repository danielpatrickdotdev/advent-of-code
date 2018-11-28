#!/usr/bin/env python3


def get_input(path):
    with open(path) as infile:
        return infile.read()


class InfiniteGrid:
    directions = ["n", "ne", "se", "s", "sw", "nw"]
    opposites = {
        "n": "s",
        "ne": "sw",
        "se": "nw",
        "s": "n",
        "sw": "ne",
        "nw": "se"
    }
    next_but_ones = {
        "n": (("se", "ne"), ("sw", "nw")),
        "ne": (("s", "se"), ("nw", "n")),
        "se": (("n", "ne"), ("sw", "s")),
        "s": (("nw", "sw"), ("ne", "se")),
        "sw": (("n", "nw"), ("se", "s")),
        "nw": (("ne", "n"), ("s", "sw"))
    }

    def get_route(self, text):
        if text:
            return [dir for dir in text.split(',')]
        else:
            return []

    def route_dict(self, route):
        counts = {k:0 for k in self.directions}
        for i in route:
              counts[i] += 1

        return counts

    def simplify_opposites(self, route_dict):
        changed = True
        while changed:
            changed = False
            for one, two in self.opposites.items():
                to_remove = min(route_dict[one], route_dict[two])
                if to_remove > 0:
                    changed = True
                route_dict[one] -= to_remove
                route_dict[two] -= to_remove
        return route_dict

    def simplify_next_but_ones(self, route_dict):
        changed = True
        while changed:
            changed = False
            for item in self.next_but_ones.keys():
                for next_but_one, middle in self.next_but_ones[item]:
                    to_convert = min(route_dict[item], route_dict[next_but_one])
                    if to_convert > 0:
                        changed = True
                    route_dict[middle] += to_convert
                    route_dict[next_but_one] -= to_convert
                    route_dict[item] -= to_convert
        return route_dict

    def simplify(self, route_list):
        route_dict = self.route_dict(route_list)
        route_dict = self.simplify_next_but_ones(route_dict)
        return self.simplify_opposites(route_dict)

    def simplify_and_count(self, route_list):
        simple_route = self.simplify(route_list)
        return sum(simple_route.values())

    def get_furthest_point_on_route(self, route_list):
        furthest = 0
        for i in range(len(route_list)):
            route = route_list[:i + 1]
            distance = self.simplify_and_count(route)
            furthest = max(furthest, distance)

        return furthest


if __name__ == '__main__':
    route_text = get_input("input.txt")
    grid = InfiniteGrid()
    route_list = grid.get_route(route_text)
    print(grid.simplify(route_list))
    print(grid.simplify_and_count(route_list))
    print("furthest point:", grid.get_furthest_point_on_route(route_list))
