use std::fs;

#[cfg(test)]
mod tests {
    #[test]
    fn test_part1() {
        let to_test: [(i32, &str); 10] = [
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
            assert_eq!(expected, &super::solve_part1(&input.to_string()));
        }
    }

    #[test]
    fn test_part2() {
        let to_test: [(i32, &str); 4] = [
            (1, ")"),
            (1, "))"),
            (3, "())"),
            (5, "()())"),
        ];

        for (expected, input) in to_test.iter() {
            assert_eq!(
                expected, &super::solve_part2(&input.to_string()).unwrap()
            );
        }

        assert!(&super::solve_part2(&String::from("")).is_none());
    }
}

fn solve_part1(puzzle_input: &String) -> i32 {
    let mut floor = 0;

    for c in puzzle_input.chars() {
        if c == '(' {
            floor += 1;
        } else if c == ')' {
            floor -= 1;
        }
    }

    floor
}

fn solve_part2(puzzle_input: &String) -> Option<i32> {
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
