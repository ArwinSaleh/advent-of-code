use std::fs::File;
use std::io::{BufRead, BufReader};

enum Direction {
    Left,  // L
    Right, // R
}

struct Step {
    direction: Direction, // L or R
    steps: i32,           // Number of steps
}

// We need on object that represents a safe's dial, it starts at 50 and goes between 0 and 99.
// One step left from 0 us 99, one step right from 99 is 0.
struct SafeDial {
    position: i32,
}

impl SafeDial {
    fn new() -> Self {
        Self { position: 50 }
    }

    fn turn(&mut self, direction: Direction, steps: i32) {
        let new_position = match direction {
            Direction::Left => self.position - steps,
            Direction::Right => self.position + steps,
        };
        self.position = new_position.rem_euclid(100);
    }

    fn get_position(&self) -> i32 {
        self.position
    }
}

fn read_input(file_path: &str) -> Vec<Step> {
    let file = File::open(file_path).expect("Failed to open file");
    let reader = BufReader::new(file);
    reader
        .lines()
        .map(|line| {
            // Line can be e.g. "L68" or "R48". Set first character as direction and rest of string as steps.
            let line_str = line.expect("Failed to read line");
            let (direction, steps) = line_str.split_at(1);
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
                steps: steps,
            }
        })
        .collect()
}

fn main() {
    let input: Vec<Step> = read_input("input.txt");
    let mut safe_dial = SafeDial::new();
    let mut num_zeroes = 0;
    for step in input {
        safe_dial.turn(step.direction, step.steps);
        let position = safe_dial.get_position();
        if position == 0 {
            num_zeroes += 1;
        }
    }
    println!("Number of zeroes: {}", num_zeroes);
}
