use std::collections::HashSet;
use std::fs;

#[derive(Debug, PartialEq, Eq, Hash)]
struct Location {
    x: i32,
    y: i32,
}

impl Location {
    fn new(x: i32, y: i32) -> Location {
        Location { x, y }
    }

    fn moved(&self, arrow: char) -> Location {
        let mut x = self.x;
        let mut y = self.y;

        match arrow {
            '>' => x += 1,
            'v' => y += 1,
            '<' => x -= 1,
            '^' => y -= 1,
            _ => panic!("You fool"),
        }

        Location::new(x, y)
    }

    fn values(&self) -> (i32, i32) {
        (self.x, self.y)
    }
}

fn solve_part1(dirs: &str) -> i32 {
    let mut loc = Location::new(0, 0);
    let mut houses = HashSet::new();
    houses.insert(loc.values());

    for d in dirs.chars() {
        loc = loc.moved(d);
        houses.insert(loc.values());
    }

    houses.len() as i32
}

fn solve_part2(dirs: &str) -> i32 {
    let mut loc1 = Location::new(0, 0);
    let mut loc2 = Location::new(0, 0);
    let mut houses = HashSet::new();
    houses.insert(loc1.values());

    for (i, d) in dirs.chars().enumerate() {
        if i % 2 == 0 {
            loc1 = loc1.moved(d);
            houses.insert(loc1.values());
        } else {
            loc2 = loc2.moved(d);
            houses.insert(loc2.values());
        }
    }

    houses.len() as i32
}

fn main() {
    #[rustfmt::skip]
    let puzzle_input = fs::read_to_string("input/input.txt")
        .expect("problem reading file");

    let result1 = solve_part1(&puzzle_input);
    println!("Part1: {}", result1);

    let result2 = solve_part2(&puzzle_input);
    println!("Part2: {}", result2);
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_move_loc() {
        let start_loc = Location::new(1, 1);
        #[rustfmt::skip]
        let test_input = [
            ('>', 2, 1),
            ('v', 1, 2),
            ('<', 0, 1),
            ('^', 1, 0)
        ];

        for (d, x, y) in test_input.iter() {
            let new_loc = start_loc.moved(*d);
            assert_eq!(*x, new_loc.x);
            assert_eq!(*y, new_loc.y);
        }
    }

    #[test]
    fn test_get_location_set() {
        #[rustfmt::skip]
        let test_input = [
            (">", 2),
            ("^>v<", 4),
            ("^v^v^v^v^v", 2),
        ];

        for (dirs, n) in test_input.iter() {
            assert_eq!(*n, solve_part1(dirs));
        }
    }

    #[test]
    fn test_part2() {
        #[rustfmt::skip]
        let test_input = [
            (">", 2),
            ("^v", 3),
            ("^>v<", 3),
            ("^v^v^v^v^v", 11),
        ];

        for (dirs, n) in test_input.iter() {
            assert_eq!(*n, solve_part2(dirs));
        }
    }
}
