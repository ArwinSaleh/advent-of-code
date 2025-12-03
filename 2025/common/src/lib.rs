use std::fs::File;
use std::io::{BufRead, BufReader};

pub enum Direction {
    Left,  // L
    Right, // R
}

pub struct Step {
    pub direction: Direction, // L or R
    pub steps: i32,           // Number of steps
}

// We need on object that represents a safe's dial, it starts at 50 and goes between 0 and 99.
// One step left from 0 us 99, one step right from 99 is 0.
pub struct SafeDial {
    position: i32,
}

impl SafeDial {
    pub fn new() -> Self {
        Self { position: 50 }
    }

    pub fn turn(&mut self, direction: Direction, steps: i32) {
        let new_position = match direction {
            Direction::Left => self.position - steps,
            Direction::Right => self.position + steps,
        };
        self.position = new_position.rem_euclid(100);
    }

    pub fn get_position(&self) -> i32 {
        self.position
    }
}

/// Reads a text file and returns a vector of strings, one per line.
///
/// # Arguments
/// * `file_path` - Path to the file to read
///
/// # Panics
/// Panics if the file cannot be opened or read.
pub fn read_lines(file_path: &str) -> Vec<String> {
    let file = File::open(file_path).expect("Failed to open file");
    let reader = BufReader::new(file);
    reader
        .lines()
        .map(|line| line.expect("Failed to read line"))
        .collect()
}

/// Parses input file into a vector of Steps.
///
/// Each line should be in the format "L68" or "R48" where the first character
/// is the direction (L or R) and the rest is the number of steps.
///
/// # Arguments
/// * `file_path` - Path to the file to read
///
/// # Panics
/// Panics if the file cannot be opened, read, or parsed.
pub fn parse_input(file_path: &str) -> Vec<Step> {
    read_lines(file_path)
        .iter()
        .map(|line| {
            // Line can be e.g. "L68" or "R48". Set first character as direction and rest of string as steps.
            let (direction, steps) = line.split_at(1);
            let direction = direction.chars().next().expect("Failed to get direction");
            let steps = steps.parse::<i32>().expect("Failed to parse steps");
            Step {
                direction: if direction == 'L' {
                    Direction::Left
                } else if direction == 'R' {
                    Direction::Right
                } else {
                    panic!("Invalid direction: {}", direction);
                },
                steps,
            }
        })
        .collect()
}
