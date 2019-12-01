use std::cmp;
use std::fs;

fn parse_file(filename: &str) -> Vec<u128> {
    fs::read_to_string(filename)
        .expect("problem reading file")
        .split('\n')
        .filter_map(|s| s.parse::<u128>().ok())
        .collect::<Vec<u128>>()
}

fn fuel_required(mass: u128) -> u128 {
    cmp::max(mass / 3, 2) - 2
}

fn fuel_required2(mass: u128) -> u128 {
    let mut fuel = fuel_required(mass);
    let mut fuel_for_the_fuel = fuel;

    while fuel_for_the_fuel > 0 {
        fuel_for_the_fuel = fuel_required(fuel_for_the_fuel);
        fuel += fuel_for_the_fuel;
    }

    fuel
}

fn solve_part1(input: &Vec<u128>) -> u128 {
    input.iter().map(|mass| fuel_required(*mass)).sum()
}

fn solve_part2(input: &Vec<u128>) -> u128 {
    input.iter().map(|mass| fuel_required2(*mass)).sum()
}

fn main() {
    let input = parse_file("input/input.txt");

    println!("{}", solve_part1(&input));
    println!("{}", solve_part2(&input));
}

// Tests

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_parse_file() {
        assert_eq!(
            parse_file("input/test_input.txt"),
            vec![12, 14, 1969, 100756]
        );
    }

    #[test]
    fn test_fuel_required() {
        assert_eq!(fuel_required(12), 2);
        assert_eq!(fuel_required(14), 2);
        assert_eq!(fuel_required(1969), 654);
        assert_eq!(fuel_required(100756), 33583);
    }

    #[test]
    fn test_fuel_required2() {
        assert_eq!(fuel_required2(12), 2);
        assert_eq!(fuel_required2(14), 2);
        assert_eq!(fuel_required2(1969), 966);
        assert_eq!(fuel_required2(100756), 50346);
    }

    #[test]
    fn test_solve_part1() {
        assert_eq!(solve_part1(&parse_file("input/test_input.txt")), 34241)
    }

    #[test]
    fn test_solve_part2() {
        assert_eq!(solve_part2(&parse_file("input/test_input.txt")), 51316)
    }
}
