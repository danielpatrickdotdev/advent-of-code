use std::fs;
use regex::Regex;


fn count_chars(test_input: &str) -> i32 {
    test_input
        .split('\n')
        .map(|s| s.chars().count() as i32)
        .sum()
}

fn unescape(test_input: &str) -> String {
    let escape_chars = ["\\", "\""];

    test_input
        .split('\n')
        .map(|s| {
            if s.len() < 2 {
                "".to_string()
            } else {
                let end = s.len() - 1;
                let new_s = &s[1..end].replace("\\\\", "..");
                new_s
                    .split('\\')
                    .enumerate()
                    .map(|(i, word)| {
                        if i == 0 || escape_chars.contains(&word) {
                            word.to_string()
                        } else {
                            if word.starts_with('x') {
                                let ord = u8::from_str_radix(&word[1..3], 16)
                                    .unwrap();
                                let c = ord as char;
                                let mut v = word
                                    .chars()
                                    .collect::<Vec<char>>();
                                v.splice(0..3, c.to_string().chars());
                                v.iter().collect::<String>()
                            } else {
                                word.to_string()
                            }
                        }
                    })
                    .collect::<Vec<String>>()
                    .join("")
                    .replace("..", "\\")
            }
        })
        .collect::<Vec<String>>()
        .join("\n")
}

fn escape(test_input: &str) -> String {
    let re = Regex::new(r"\\(?P<hex>x[0-9a-f]{2})").unwrap();

    test_input
        .split('\n')
        .map(|s| {
            if s.len() > 0 {
                let mut s1 = s
                    .replace("\\\\", "--------")
                    .replace("\\\"", "----....")
                    .replace("\\\\", "--------")
                    .replace("\\\\", "--------");

                s1 = re.replace_all(&s1, "----$hex").to_string();

                let mut s2 = String::from("\"....");
                s2.push_str(&s1[1..s1.len()-1]);
                s2.push_str(&"....\"");

                s2 = s2
                    .replace("----", "\\\\")
                    .replace("....", "\\\"");
                s2.to_string()
            } else {
                s.to_string()
            }
        })
        .collect::<Vec<String>>()
        .join("\n")
}

fn solve_part1(puzzle_input: &str) -> i32 {
    count_chars(&puzzle_input) - count_chars(&unescape(&puzzle_input))
}

fn solve_part2(puzzle_input: &str) -> i32 {
    count_chars(&escape(&puzzle_input)) - count_chars(&puzzle_input)
}

fn main() {
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

    fn example_input() -> String {
        String::from(
            "\"\"\n\
             \"abc\"\n\
             \"aaa\\\"aaa\"\n\
             \"\\x27\"\n"
        )
    }

    fn create_test_input() -> String {
        String::from(
            "\"\"\n\
             \"a\"\n\
             \"abc\"\n\
             \"aaa\\\"aaa\"\n\
             \"bbb\\\\bbb\"\n\
             \"\\x27\"\n"
        )
    }

    #[test]
    fn test_count_chars() {
        let test_input = create_test_input();
        let num_chars = count_chars(&test_input);

        assert_eq!(num_chars, 36);
    }

    #[test]
    fn test_count_chars_with_example_input() {
        let test_input = example_input();
        let num_chars = count_chars(&test_input);

        assert_eq!(num_chars, 23);
    }

    #[test]
    fn test_count_chars_with() {
        let test_input = create_test_input();
        let num_chars = count_chars(&test_input);

        assert_eq!(num_chars, 36);
    }

    #[test]
    fn test_unescape() {
        let test_input = create_test_input();
        let unescaped = unescape(&test_input);

        assert_eq!(unescaped, "\na\nabc\naaa\"aaa\nbbb\\bbb\n'\n");
        assert_eq!(count_chars(&unescaped), 19);
    }

    #[test]
    fn test_escape() {
        let test_input = create_test_input();
        let escaped = escape(&test_input);
        let expected = "\"\\\"\\\"\"\n\
                        \"\\\"a\\\"\"\n\
                        \"\\\"abc\\\"\"\n\
                        \"\\\"aaa\\\\\\\"aaa\\\"\"\n\
                        \"\\\"bbb\\\\\\\\bbb\\\"\"\n\
                        \"\\\"\\\\x27\\\"\"\n";

        assert_eq!(escaped, expected);
        assert_eq!(count_chars(&escaped), 65);
    }

    #[test]
    fn test_part1() {
        let test_input = create_test_input();

        assert_eq!(solve_part1(&test_input), 17);
    }

    #[test]
    fn test_part1_with_example_input() {
        let test_input = example_input();

        assert_eq!(solve_part1(&test_input), 12);
    }

    #[test]
    fn test_part2() {
        let test_input = create_test_input();

        assert_eq!(solve_part2(&test_input), 29);
    }

    #[test]
    fn test_part2_with_example_input() {
        let test_input = example_input();

        assert_eq!(solve_part2(&test_input), 19);
    }
}
