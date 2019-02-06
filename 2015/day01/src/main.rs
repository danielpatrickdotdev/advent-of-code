use std::fs;

fn solve_part1(puzzle_input: &str) -> i32 {
    puzzle_input
        .chars()
        .map(|c| match c {
            '(' => 1,
            ')' => -1,
            _ => 0,
        })
        .sum()
}

fn solve_part2(puzzle_input: &str) -> Option<i32> {
    let mut floor = 0;

    for (i, c) in puzzle_input.chars().enumerate()  {
        if c == '(' {
            floor += 1;
        } else if c == ')' {
            floor -= 1;
        }
        if floor < 0 {
            return Some(i as i32 + 1)
        }
    }

    None
}

fn main() {
    let puzzle_input = fs::read_to_string("input/input.txt")
        .expect("problem reading file");

    let result1 = solve_part1(&puzzle_input);
    println!("Part1: {}", result1);

    let result2 = solve_part2(&puzzle_input);
    println!("Part2: {}", result2.unwrap());
}

#[cfg(test)]
mod tests {
    #[test]
    fn test_part1() {
        let to_test = [
            (0, ""),
            (0, "(())"),
            (0, "()()"),
            (3, "((("),
            (3, "(()(()("),
            (3, "))((((("),
            (-1, "())"),
            (-1, "))("),
            (-3, ")))"),
            (-3, ")())())"),
        ];
        for (expected, input) in to_test.iter() {
            assert_eq!(expected, &super::solve_part1(&input));
        }
    }

    #[test]
    fn test_part2() {
        let to_test = [
            (1, ")"),
            (1, "))"),
            (3, "())"),
            (5, "()())"),
        ];

        for (expected, input) in to_test.iter() {
            assert_eq!(
                expected, &super::solve_part2(&input).unwrap()
            );
        }

        assert!(&super::solve_part2("").is_none());
    }
}
