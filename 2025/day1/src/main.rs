use common::{parse_input, SafeDial};

const ANSWER: i32 = 1036;

fn main() {
    let input = parse_input("../common/input.txt");
    let mut safe_dial = SafeDial::new();
    let mut num_zeroes = 0;
    for step in input {
        safe_dial.turn(step.direction, step.steps);
        let position = safe_dial.get_position();
        if position == 0 {
            num_zeroes += 1;
        }
    }
    assert_eq!(num_zeroes, ANSWER);
    println!("Answer: {}", num_zeroes);
}
