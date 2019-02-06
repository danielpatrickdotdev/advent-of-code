use std::fs;
mod present;
use self::present::Present;

fn solve_part1(puzzle_input: &str) -> i32 {
    puzzle_input
        .lines()
        .map(|line| Present::new(line))
        .map(|present| present.wrapping_paper_required())
        .sum()
}

fn solve_part2(puzzle_input: &str) -> i32 {
    puzzle_input
        .lines()
        .map(|line| Present::new(line))
        .map(|present| present.ribbon_required())
        .sum()
}

fn main() {
    #[rustfmt::skip]
    let puzzle_input = fs::read_to_string("input/input.txt")
        .expect("problem reading file");

    println!("Part1: {}", solve_part1(&puzzle_input));

    println!("Part2: {}", solve_part2(&puzzle_input));
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_part1() {
        let test_input = "2x3x4\n1x1x10";

        assert_eq!(101, solve_part1(&test_input));
    }

    #[test]
    fn test_part2() {
        let test_input = "2x3x4\n1x1x10";

        assert_eq!(48, solve_part2(&test_input));
    }
}
