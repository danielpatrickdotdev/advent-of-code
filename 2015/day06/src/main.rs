extern crate itertools;
extern crate regex;

use std::cmp::max;
use std::fs;

use itertools::Itertools;
use regex::Regex;

#[derive(Debug, PartialEq)]
enum InstructionType {
    TurnOn,
    TurnOff,
    Toggle,
}

#[derive(Debug)]
struct Instruction {
    instruction_type: InstructionType,
    start_x: i32,
    start_y: i32,
    end_x: i32,
    end_y: i32,
}

impl Instruction {
    fn new(
        instruction_type: InstructionType,
        start_x: i32,
        start_y: i32,
        end_x: i32,
        end_y: i32,
    ) -> Instruction {
        Instruction {
            instruction_type,
            start_x,
            start_y,
            end_x,
            end_y,
        }
    }

    fn act(&self, x: i32, y: i32, is_on: bool) -> bool {
        if (x >= self.start_x) & (x <= self.end_x) & (y >= self.start_y) & (y <= self.end_y) {
            match self.instruction_type {
                InstructionType::TurnOn => true,
                InstructionType::TurnOff => false,
                InstructionType::Toggle => !is_on,
            }
        } else {
            is_on
        }
    }

    fn act2(&self, x: i32, y: i32, prev: i32) -> i32 {
        if (x >= self.start_x) & (x <= self.end_x) & (y >= self.start_y) & (y <= self.end_y) {
            match self.instruction_type {
                InstructionType::TurnOn => prev + 1,
                InstructionType::TurnOff => max(prev - 1, 0),
                InstructionType::Toggle => prev + 2,
            }
        } else {
            prev
        }
    }
}

fn parse_instruction(instruction_str: &str) -> Instruction {
    let re =
        Regex::new(r"^(turn on|turn off|toggle) (\d{1,3}),(\d{1,3}) through (\d{1,3}),(\d{1,3})$")
            .unwrap();
    let capture = re.captures(instruction_str).unwrap();
    let instr_type = match &capture[1] {
        "turn on" => InstructionType::TurnOn,
        "turn off" => InstructionType::TurnOff,
        "toggle" => InstructionType::Toggle,
        _ => panic!("Surprise! (unexpected string matched)"),
    };
    Instruction::new(
        instr_type,
        capture[2].parse().unwrap(),
        capture[3].parse().unwrap(),
        capture[4].parse().unwrap(),
        capture[5].parse().unwrap(),
    )
}

fn parse_instructions(puzzle_input: &str) -> Vec<Instruction> {
    puzzle_input.lines().map(|s| parse_instruction(s)).collect()
}

// Part 1

fn solve_part1(puzzle_input: &str) -> usize {
    let instructions = parse_instructions(puzzle_input);

    (0..1000)
        .cartesian_product(0..1000)
        .filter(|(x, y)| {
            instructions
                .iter()
                .fold(false, |acc, instr| instr.act(*x, *y, acc))
        })
        .count()
}

// Part 2

fn solve_part2(puzzle_input: &str) -> i32 {
    let instructions = parse_instructions(puzzle_input);

    (0..1000)
        .cartesian_product(0..1000)
        .map(|(x, y)| {
            instructions
                .iter()
                .fold(0, |acc, instr| instr.act2(x, y, acc))
        })
        .sum()
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
    use super::InstructionType::{Toggle, TurnOff, TurnOn};
    use super::*;

    #[test]
    fn test_act() {
        let turn_on = Instruction::new(TurnOn, 0, 0, 500, 500);
        let toggle = Instruction::new(Toggle, 0, 0, 500, 500);
        let turn_off = Instruction::new(TurnOff, 0, 0, 500, 500);

        #[rustfmt::skip]
        let to_test = [
            (&turn_on, 0, 500, true, true),
            (&turn_on, 0, 500, false, true),
            (&turn_on, 0, 501, false, false),
            (&turn_on, 0, 501, true, true),
            (&toggle, 500, 0, true, false),
            (&toggle, 500, 0, false, true),
            (&toggle, 501, 0, false, false),
            (&toggle, 501, 0, true, true),
            (&turn_off, 0, 0, true, false),
            (&turn_off, 500, 500, false, false),
            (&turn_off, 0, 0, false, false),
            (&turn_off, 501, 501, true, true),
        ];

        for (instruction, x, y, is_on, expected) in to_test.iter() {
            assert_eq!(*expected, instruction.act(*x, *y, *is_on));
        }
    }

    #[test]
    fn test_parse_instruction() {
        #[rustfmt::skip]
        let test_input = [
            ("turn on 0,0 through 999,999", TurnOn, 0, 0, 999, 999),
            ("toggle 0,0 through 999,0", Toggle, 0, 0, 999, 0),
            ("turn off 499,499 through 500,500", TurnOff, 499, 499, 500, 500),
        ];

        for (i_str, i_type, start_x, start_y, end_x, end_y) in test_input.iter() {
            let instruction = parse_instruction(i_str);
            assert_eq!(*i_type, instruction.instruction_type);
            assert_eq!(*start_x, instruction.start_x);
            assert_eq!(*start_y, instruction.start_y);
            assert_eq!(*end_x, instruction.end_x);
            assert_eq!(*end_y, instruction.end_y);
        }
    }

    #[test]
    fn test_parse_instructions() {
        #[rustfmt::skip]
        let test_input = "turn on 0,0 through 999,999\n\
                          toggle 0,0 through 999,0\n\
                          turn off 499,499 through 500,500";
        let expected_values = [
            (TurnOn, 0, 0, 999, 999),
            (Toggle, 0, 0, 999, 0),
            (TurnOff, 499, 499, 500, 500),
        ];

        let instructions = parse_instructions(test_input);

        for (instruction, expected) in instructions.iter().zip(&expected_values) {
            let (i_type, start_x, start_y, end_x, end_y) = expected;
            assert_eq!(*i_type, instruction.instruction_type);
            assert_eq!(*start_x, instruction.start_x);
            assert_eq!(*start_y, instruction.start_y);
            assert_eq!(*end_x, instruction.end_x);
            assert_eq!(*end_y, instruction.end_y);
        }
    }

    #[test]
    fn test_part1() {
        #[rustfmt::skip]
        let test_input = "turn on 0,0 through 99,99\n\
                          toggle 0,0 through 999,0\n\
                          turn off 99,99 through 100,100";

        assert_eq!(10_799 as usize, solve_part1(&test_input));
    }

    #[test]
    fn test_part2() {
        #[rustfmt::skip]
        let test_input = "turn on 0,0 through 99,99\n\
                          toggle 0,0 through 999,0\n\
                          turn off 99,99 through 100,100";

        assert_eq!(11_999, solve_part2(&test_input));
    }
}
