#!/usr/bin/env python
# -*- coding: utf-8 -*-

from operator import attrgetter, itemgetter


class CombatantBaseClass:
    letter = None

    def __init__(self, x, y):
        self.is_dead = False
        self.hit_points = 200
        self.attack_power = 3
        self.x = x
        self.y = y

    def get_location(self):
        return (self.x, self.y)

    def move(self, x, y):
        self.x = x
        self.y = y

    def damage(self, power):
        self.hit_points = max(0, self.hit_points - power)
        self.is_dead = self.hit_points == 0

    def attack(self, other):
        other.damage(self.attack_power)

    def __str__(self):
        return self.letter


class Elf(CombatantBaseClass):
    letter = "E"


class Goblin(CombatantBaseClass):
    letter = "G"


class Caves:
    def __init__(self, data):
        self.grid = []
        self.goblins = []
        self.elves = []
        self.height = len(data)
        self.width = len(data[0])

        for x in range(self.width):
            col = []
            self.grid.append(col)

            for y in range(self.height):
                cell_contents = data[y][x]

                if cell_contents == "G":
                    new_goblin = Goblin(x, y)
                    self.goblins.append(new_goblin)
                    col.append(new_goblin)
                elif cell_contents == "E":
                    new_elf = Elf(x, y)
                    self.elves.append(new_elf)
                    col.append(new_elf)
                else:
                    col.append(cell_contents)

        self.sort()

    def set(self, x, y, value):
        self.grid[x][y] = value

    def get(self, x, y):
        return self.grid[x][y]

    def sort(self):
        self.elves.sort(key=attrgetter("y", "x"))
        self.goblins.sort(key=attrgetter("y", "x"))

    def opponents(self, combatant):
        return self.elves if str(combatant) == "G" else self.goblins

    def in_range(self, combatant, opponent):
        x1, y1 = combatant.get_location()
        x2, y2 = opponent.get_location()
        return (abs(x1 - x2) + abs(y1 - y2)) <= 1

    def in_grid(self, x, y):
        return 0 <= x < self.width and 0 <= y < self.height

    def get_squares_in_range(self, x, y):
        return [
            coord for coord in [(x, y - 1), (x - 1, y), (x + 1, y), (x, y + 1)]
            if self.in_grid(*coord)
        ]

    def is_empty(self, x, y, grid=None):
        if grid is None:
            grid = self.grid

        return grid[x][y] == "."

    def get_open_squares_in_range(self, x, y, grid=None):
        if grid is None:
            grid = self.grid

        return [
            coord for coord in self.get_squares_in_range(x, y)
            if self.is_empty(*coord, grid)
        ]

    def get_target_squares(self, combatant):
        opponents = self.opponents(combatant)

        if any(self.in_range(combatant, opponent) for opponent in opponents):
            return None

        targets = set()

        for opponent in opponents:
            targets.update(
                self.get_open_squares_in_range(*opponent.get_location())
            )

        return sorted(list(targets), key=itemgetter(1, 0))

    def get_best_move(self, combatant, opponents=None):
        targets = self.get_target_squares(combatant)

        if not targets or self.is_trapped(combatant, targets):
            return None

        potential_moves = self.get_open_squares_in_range(
            *combatant.get_location()
        )

        best_moves = {}
        best_move = None

        for x, y in targets:
            grid_copy = [col[:] for col in self.grid]

            current_layer = set([(x, y)])
            n = 0

            # Stop when we run out of moves to explore or we've reached the
            # number of moves at which we already found a higher priority target
            while current_layer and (best_move is None or best_move > n):
                next_layer = set()

                for (x, y) in current_layer:
                    if (x, y) in potential_moves:
                        best_move = n
                        best_moves[(x, y)] = n

                    grid_copy[x][y] = n

                    next_layer.update(
                        self.get_open_squares_in_range(x, y, grid_copy) or []
                    )

                current_layer = next_layer
                n += 1

        # Get best moves and rank by UP, LEFT, RIGHT, DOWN
        moves = [key for key, value in best_moves.items() if value == best_move]

        if not moves:
            return None

        moves.sort(key=itemgetter(1, 0))
        return moves[0]

    def move_combatant(self, combatant):
        best_move = self.get_best_move(combatant)

        if best_move is not None:
            x, y = combatant.get_location()
            self.grid[x][y] = "."

            x, y = best_move
            self.grid[x][y] = combatant
            combatant.move(x, y)

    def is_trapped(self, combatant, targets):
        grid_copy = [col[:] for col in self.grid]

        current_layer = [combatant.get_location()]

        while current_layer:
            next_layer = set()

            for (x, y) in current_layer:
                if (x, y) in targets:
                    return False

                grid_copy[x][y] = "X"

                next_layer.update(
                    self.get_open_squares_in_range(x, y, grid_copy) or []
                )

            current_layer = next_layer

        return True

    def get_opponents_within_range(self, combatant):
        opposing_letter = "G" if str(combatant) == "E" else "E"

        in_range = [
            self.get(x, y) for (x, y) in self.get_squares_in_range(
                *combatant.get_location()
            ) if str(self.get(x, y)) == opposing_letter
        ]

        return sorted(in_range, key=attrgetter("hit_points", "y", "x"))

    def attack(self, combatant, opponent):
        combatant.attack(opponent)

        if opponent.is_dead:
            x, y = opponent.get_location()
            # Remove from grid
            self.grid[x][y] = "."

            # Remove from self.elves/self.goblins
            if str(opponent) == "E":
                self.elves.remove(opponent)
            else:
                self.goblins.remove(opponent)

    def advance(self):
        combatants = self.elves + self.goblins
        combatants.sort(key=attrgetter("y", "x"))
        game_over = False

        for combatant in combatants:
            if not self.opponents(combatant):
                game_over = True

            if combatant.is_dead:
                continue

            self.move_combatant(combatant)

            opponents = self.get_opponents_within_range(combatant)

            if opponents:
                self.attack(combatant, opponents[0])

        self.sort()
        return game_over

    def __str__(self):
        return "\n".join(
            "".join(
                str(self.grid[x][y]) for x in range(self.width)
            ) for y in range(self.height)
        )
