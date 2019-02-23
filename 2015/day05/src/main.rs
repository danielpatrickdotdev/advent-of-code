use std::collections::HashMap;
use std::fs;

extern crate itertools;
use itertools::Itertools;

// Part 1

fn has_three_vowels(s: &str) -> bool {
    s.chars().filter(|c| "aeiou".contains(*c)).count() >= 3
}

fn has_repeated_char(s: &str) -> bool {
    s.chars().tuple_windows::<(_, _)>().any(|(a, b)| a == b)
}

fn has_illegal_strings(s: &str) -> bool {
    s.contains("ab") | s.contains("cd") | s.contains("pq") | s.contains("xy")
}

fn is_nice_part1(s: &str) -> bool {
    has_three_vowels(s) & has_repeated_char(s) & !has_illegal_strings(s)
}

fn solve_part1(strings: &str) -> usize {
    strings.lines().filter(|s| is_nice_part1(s)).count()
}

// Part 2

fn has_two_pairs(s: &str) -> bool {
    let mut pairs: HashMap<(char, char), Vec<usize>> = HashMap::new();

    for ((i, c1), (_, c2)) in s.chars().enumerate().tuple_windows::<(_, _)>() {
        let positions = pairs.entry((c1, c2)).or_insert_with(Vec::new);
        positions.push(i);
    }

    pairs.values().any(|val| {
        val.iter()
            .tuple_combinations()
            .any(|(a, b)| (*a as i32 - *b as i32).abs() > 1)
    })
}

fn has_split_repeat(s: &str) -> bool {
    s.chars()
        .tuple_windows::<(_, _, _)>()
        .any(|(a, _b, c)| a == c)
}

fn is_nice_part2(s: &str) -> bool {
    has_two_pairs(s) & has_split_repeat(s)
}

fn solve_part2(strings: &str) -> usize {
    strings.lines().filter(|s| is_nice_part2(s)).count()
}

// Main

fn main() {
    #[rustfmt::skip]
    let puzzle_input = fs::read_to_string("input/input.txt")
        .expect("problem reading file");

    let result1 = solve_part1(&puzzle_input);
    println!("Part1: {}", result1);

    let result2 = solve_part2(&puzzle_input);
    println!("Part2: {}", result2);
}

// Tests

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_has_three_vowels() {
        let test_input = [
            ("aeiou", true),
            ("aei", true),
            ("xazegov", true),
            ("aeiouaeiouaeiou", true),
            ("xx", false),
            ("iijjkk", false),
            ("arrgh", false),
            ("abcdde", false),
            ("aabbccdd", false),
            ("ooppqq", false),
            ("wwxxyyzz", false),
        ];

        for (s, expected) in test_input.iter() {
            assert_eq!(*expected, has_three_vowels(s));
        }
    }

    #[test]
    fn test_has_repeated_char() {
        let test_input = [
            ("aeiou", false),
            ("aei", false),
            ("xazegov", false),
            ("aeiouaeiouaeiou", false),
            ("xx", true),
            ("iijjkk", true),
            ("arrgh", true),
            ("abcdde", true),
            ("aabbccdd", true),
            ("ooppqq", true),
            ("wwxxyyzz", true),
        ];

        for (s, expected) in test_input.iter() {
            assert_eq!(*expected, has_repeated_char(s));
        }
    }

    #[test]
    fn test_has_illegal_strings() {
        let test_input = [
            ("aeiou", false),
            ("aei", false),
            ("xazegov", false),
            ("aeiouaeiouaeiou", false),
            ("xx", false),
            ("iijjkk", false),
            ("arrgh", false),
            ("abcdde", true),
            ("aabbccdd", true),
            ("ooppqq", true),
            ("wwxxyyzz", true),
        ];

        for (s, expected) in test_input.iter() {
            assert_eq!(*expected, has_illegal_strings(s));
        }
    }

    #[test]
    fn test_is_nice_part1() {
        #[rustfmt::skip]
        let test_input = [
            ("ugknbfddgicrmopn", true),
            ("aaa", true),
            ("jchzalrnumimnmhp", false),
            ("haegwjzuvuyypxyu", false),
            ("dvszwmarrgswjxmb", false),
        ];

        for (s, expected) in test_input.iter() {
            assert_eq!(*expected, is_nice_part1(s));
        }
    }

    #[test]
    fn test_part1() {
        #[rustfmt::skip]
        let test_input = "ugknbfddgicrmopn\n\
                          aaa\n\
                          jchzalrnumimnmhp\n\
                          haegwjzuvuyypxyu\n\
                          dvszwmarrgswjxmb";

        assert_eq!(2 as usize, solve_part1(&test_input));
    }

    #[test]
    fn test_has_two_pairs() {
        #[rustfmt::skip]
        let test_input = [
            ("xyxy", true),
            ("aabcdefgaa", true),
            ("baaa", false),
        ];

        for (s, expected) in test_input.iter() {
            assert_eq!(*expected, has_two_pairs(s));
        }
    }

    #[test]
    fn test_has_split_repeat() {
        #[rustfmt::skip]
        let test_input = [
            ("xyx", true),
            ("abcdefeghi", true),
            ("aaa", true),
            ("baab", false),
        ];

        for (s, expected) in test_input.iter() {
            assert_eq!(*expected, has_split_repeat(s));
        }
    }

    #[test]
    fn test_is_nice_part2() {
        #[rustfmt::skip]
        let test_input = [
            ("qjhvhtzxzqqjkmpb", true),
            ("xxyxx", true),
            ("uurcxstgmygtbstg", false),
            ("ieodomkazucvgmuy", false),
        ];

        for (s, expected) in test_input.iter() {
            assert_eq!(*expected, is_nice_part2(s));
        }
    }

    #[test]
    fn test_part2() {
        #[rustfmt::skip]
        let test_input = "qjhvhtzxzqqjkmpb\n\
                          xxyxx\n\
                          uurcxstgmygtbstg\n\
                          ieodomkazucvgmuy";

        assert_eq!(2 as usize, solve_part2(&test_input));
    }
}
