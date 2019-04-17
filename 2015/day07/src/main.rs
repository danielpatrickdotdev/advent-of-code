use std::collections::HashMap;
use std::fs;

#[derive(Debug, PartialEq)]
enum Instruction<'a> {
    Noop(&'a str),
    Not(&'a str),
    And(&'a str, &'a str),
    Or(&'a str, &'a str),
    Lshift(&'a str, u16),
    Rshift(&'a str, u16),
}

impl<'a> Instruction<'a> {
    fn new(words: Vec<&'a str>) -> Instruction<'a> {
        if words.len() == 1 {
            return Instruction::Noop(words[0]);
        }
        if words[0] == "NOT" {
            return Instruction::Not(words[1]);
        }
        match words[1] {
            "AND" => Instruction::And(words[0], words[2]),
            "OR" => Instruction::Or(words[0], words[2]),
            "LSHIFT" => Instruction::Lshift(words[0], words[2].parse::<u16>().unwrap()),
            "RSHIFT" => Instruction::Rshift(words[0], words[2].parse::<u16>().unwrap()),
            _ => panic!("Cannot parse invalid instruction {}", &words.join(" ")),
        }
    }
}

fn parse_instructions<'a>(input: &'a str) -> HashMap<&'a str, Instruction> {
    input
        .lines()
        .map(|s| {
            let mut value: Vec<&str> = s.split(' ').collect();
            let key = value.pop().expect("Empty instruction?");
            value.pop();
            (key, Instruction::new(value))
        })
        .collect()
}

fn resolve_value(value: &str, register: &HashMap<&str, u16>) -> Option<u16> {
    value
        .parse::<u16>()
        .ok()
        .or(register.get(value).map(|v| v.to_owned()))
}

fn resolve(instruction: &Instruction, register: &HashMap<&str, u16>) -> Option<u16> {
    match instruction {
        Instruction::Noop(a) => resolve_value(a, register),
        Instruction::Not(a) => resolve_value(a, register).map(|v| !v),
        Instruction::And(a, b) => {
            resolve_value(a, register).and_then(|v| resolve_value(b, register).map(|u| v & u))
        }
        Instruction::Or(a, b) => {
            resolve_value(a, register).and_then(|v| resolve_value(b, register).map(|u| v | u))
        }
        Instruction::Lshift(a, b) => resolve_value(a, register).map(|v| v << b),
        Instruction::Rshift(a, b) => resolve_value(a, register).map(|v| v >> b),
    }
}

fn process_instructions<'a, 'b>(
    instructions: &HashMap<&'a str, Instruction>,
) -> HashMap<&'a str, u16> {
    let mut registers = HashMap::new();

    while registers.len() < instructions.len() {
        let mut progress = false;

        for (reg, instruction) in instructions.iter() {
            if registers.contains_key(reg) {
                continue;
            }

            if let Some(val) = resolve(instruction, &registers) {
                &registers.insert(reg, val);
                progress = true;
            }
        }

        if !progress {
            break;
        }
    }

    registers
}

// Part 1

fn solve_part1(puzzle_input: &str) -> u16 {
    let instructions = parse_instructions(&puzzle_input);
    let registers = process_instructions(&instructions);

    *registers.get("a").unwrap()
}

// Part 2

fn solve_part2(puzzle_input: &str) -> u16 {
    let mut instructions = parse_instructions(&puzzle_input);
    let registers = process_instructions(&instructions);

    let a = registers["a"].to_string();
    instructions.insert("b", Instruction::Noop(&a));
    let new_registers = process_instructions(&instructions);

    *new_registers.get("a").unwrap()
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

    fn create_test_input() -> String {
        String::from(
            "123 -> a\n\
             456 -> b\n\
             a AND b -> c\n\
             a OR b -> d\n\
             a LSHIFT 2 -> e\n\
             b RSHIFT 2 -> f\n\
             NOT a -> g\n\
             NOT b -> h",
        )
    }

    #[test]
    fn test_parse_instructions() {
        let test_input = create_test_input();
        let instructions = parse_instructions(&test_input);

        assert_eq!(instructions.len(), 8);
        assert_eq!(instructions["a"], Instruction::Noop("123"));
        assert_eq!(instructions["b"], Instruction::Noop("456"));
        assert_eq!(instructions["c"], Instruction::And("a", "b"));
        assert_eq!(instructions["d"], Instruction::Or("a", "b"));
        assert_eq!(instructions["e"], Instruction::Lshift("a", 2));
        assert_eq!(instructions["f"], Instruction::Rshift("b", 2));
        assert_eq!(instructions["g"], Instruction::Not("a"));
        assert_eq!(instructions["h"], Instruction::Not("b"));
    }

    #[test]
    fn test_new_instruction() {
        #[rustfmt::skip]
        let test_values = [
            (vec!["123"], Instruction::Noop("123")),
            (vec!["b"], Instruction::Noop("b")),
            (vec!["NOT", "b"], Instruction::Not("b")),
            (vec!["a", "AND", "123"], Instruction::And("a", "123")),
            (vec!["123", "OR", "b"], Instruction::Or("123", "b")),
            (vec!["a", "LSHIFT", "2"], Instruction::Lshift("a", 2)),
            (vec!["a", "RSHIFT", "2"], Instruction::Rshift("a", 2)),
        ];

        for (input, output) in test_values.iter() {
            assert_eq!(Instruction::new(input.to_owned()), *output);
        }
    }

    #[test]
    fn test_process_instructions() {
        #[rustfmt::skip]
        let mut test_input = HashMap::new();
        test_input.insert("a", Instruction::Noop("123"));
        test_input.insert("b", Instruction::Noop("456"));
        test_input.insert("c", Instruction::And("a", "b"));
        test_input.insert("d", Instruction::Or("a", "b"));
        test_input.insert("e", Instruction::Lshift("a", 2));
        test_input.insert("f", Instruction::Rshift("b", 2));
        test_input.insert("g", Instruction::Not("a"));
        test_input.insert("h", Instruction::Not("b"));

        let registers = process_instructions(&test_input);

        println!("registers: {:#?}", registers);
        assert_eq!(123 as u16, registers["a"]);
        assert_eq!(456 as u16, registers["b"]);
        assert_eq!(72 as u16, registers["c"]);
        assert_eq!(507 as u16, registers["d"]);
        assert_eq!(492 as u16, registers["e"]);
        assert_eq!(114 as u16, registers["f"]);
        assert_eq!(65412 as u16, registers["g"]);
        assert_eq!(65079 as u16, registers["h"]);
    }

    #[test]
    fn test_part1() {
        #[rustfmt::skip]
        let test_input = "123 -> a\n\
                          456 -> b\n\
                          a AND b -> c\n\
                          a OR b -> d\n\
                          a LSHIFT 2 -> e\n\
                          b RSHIFT 2 -> f\n\
                          NOT a -> g\n\
                          NOT b -> h";

        assert_eq!(123 as u16, solve_part1(&test_input));
    }

    #[test]
    fn test_part2() {
        #[rustfmt::skip]

        let test_input = "h -> a\n\
                          456 -> b\n\
                          a AND b -> c\n\
                          a OR b -> d\n\
                          a LSHIFT 2 -> e\n\
                          b RSHIFT 2 -> f\n\
                          NOT a -> g\n\
                          NOT b -> h";

        assert_eq!(456 as u16, solve_part2(&test_input));
    }
}
