use std::env;
use std::fs;


fn all_different_characters<Char>(char_buffer: Vec<char>) -> bool {
    let mut last_char: char = '.';
    let mut sorted_char_buffer = char_buffer;
    sorted_char_buffer.sort();
    for c in sorted_char_buffer {
        if last_char == c {
            return false;
        }
        last_char = c;
    }
    return true;
}

fn decode_signal(char_buffer_length: usize) -> usize {
    // Read input.
    let args: Vec<String> = env::args().collect();
    let file_path: &String = &args[1];
    let contents: String = fs::read_to_string(file_path)
        .expect("Should have been able to read the file");

    let mut n_processed_chars: usize = 0;
    let mut char_buffer: Vec<char> = Vec::new();
    for c in contents.chars() {
        char_buffer.push(c);
        n_processed_chars += 1;
        if char_buffer.len() > char_buffer_length {
            char_buffer.remove(0);
        }
        if all_different_characters::<char>(char_buffer.clone()) && char_buffer.len() == char_buffer_length {
            break;
        }
    }
    return n_processed_chars;
}

fn main() {
    
    // Part 1.
    let n_chars_part1: usize = decode_signal(4);

    // Part 2.
    let n_chars_part2: usize = decode_signal(14);

    // Output.
    println!("Part 1: {}", n_chars_part1);
    println!("Part 2: {}", n_chars_part2);
}
