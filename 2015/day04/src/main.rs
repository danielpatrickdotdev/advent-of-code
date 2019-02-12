extern crate md5;

fn starts_with_n_zeroes(input: &str, n: usize) -> bool {
    input.len() >= n && input[0..n].chars().all(|c| c == '0')
}

fn solve(puzzle_input: &str, num_zeroes: usize) -> i32 {
    let mut n = 0;

    loop {
        n += 1;
        let to_hash = format!("{}{}", puzzle_input, n);
        let digest = md5::compute(to_hash);

        if starts_with_n_zeroes(&format!("{:x}", digest), num_zeroes) {
            return n;
        }
    }
}

fn solve_part1(puzzle_input: &str) -> i32 {
    solve(puzzle_input, 5)
}

fn solve_part2(puzzle_input: &str) -> i32 {
    solve(puzzle_input, 6)
}

fn main() {
    let puzzle_input = "ckczppom";

    let result1 = solve_part1(&puzzle_input);
    println!("Part1: {}", result1);

    let result2 = solve_part2(&puzzle_input);
    println!("Part2: {}", result2);
}

#[cfg(test)]
mod tests {
    #[test]
    fn test_starts_with_n_zeroes() {
        #[rustfmt::skip]
        let should_be_false = [
            ("", 5),
            ("0", 5),
            ("0000", 5),
            ("0000-", 5),
            ("100000", 5),
            ("00000", 6),
        ];
        for (input, n) in should_be_false.iter() {
            assert!(!super::starts_with_n_zeroes(&input, *n));
        }

        #[rustfmt::skip]
        let should_be_true = [
            ("00000", 5),
            ("000001", 5),
            ("000000", 6),
            ("0000001", 6),
        ];
        for (input, n) in should_be_true.iter() {
            assert!(super::starts_with_n_zeroes(&input, *n));
        }
    }

    #[test]
    fn test_part1() {
        #[rustfmt::skip]
        let to_test = [
            ("abcdef", 609043),
            ("pqrstuv", 1048970),
        ];
        for (input, expected) in to_test.iter() {
            assert_eq!(expected, &super::solve_part1(&input));
        }
    }
}
