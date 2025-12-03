from argparse import ArgumentParser
from pathlib import Path
from typing import List, Dict


argument_parser = ArgumentParser()
argument_parser.add_argument(
    "--input",
    help="Input to file containing drawing of stacks.",
    type=Path,
    required=True,
)
parsed_args = argument_parser.parse_args()

NEW_LINE = "\n"
DELIMITER = " "
CHARS_PER_CRATE = 4


class CrateMover:
    def __init__(self, n_stacks) -> None:
        self.n_stacks = n_stacks
        self.crate_stacks: Dict[List[str]] = {}

    def move_crates_9000(self, n_crates: int, source_stack: int, target_stack: int):
        for _ in range(n_crates):
            self.crate_stacks[target_stack - 1].append(
                self.crate_stacks[source_stack - 1].pop()
            )

    def move_crates_9001(self, n_crates: int, source_stack: int, target_stack: int):
        tmp_stack = []
        for _ in range(n_crates):
            tmp_stack.append(self.crate_stacks[source_stack - 1].pop())
        tmp_stack.reverse()
        self.crate_stacks[target_stack - 1].extend(tmp_stack)

    def parse_crates(self, line: str):
        non_stack_chars = [str(stack_idx) for stack_idx in range(1, self.n_stacks + 1)]
        non_stack_chars.append(" ")
        for i in range(self.n_stacks):
            if i not in self.crate_stacks.keys():
                self.crate_stacks[i] = []
            crate_char = line[1 + i * CHARS_PER_CRATE]
            if crate_char not in non_stack_chars:
                self.crate_stacks[i].append(crate_char)

    def reverse_stacks(self):
        for i, _ in enumerate(self.crate_stacks):
            self.crate_stacks[i].reverse()


def get_stack_drawing(input_file_path: Path) -> List[str]:
    with open(input_file_path, "r") as input_file:
        stack_drawing = input_file.readlines()
    return stack_drawing


if __name__ == "__main__":
    stack_drawing = get_stack_drawing(parsed_args.input)
    n_stacks = len(stack_drawing[0]) // CHARS_PER_CRATE

    CrateMover_9000 = CrateMover(n_stacks)
    CrateMover_9001 = CrateMover(n_stacks)

    line_is_instruction = False
    for line in stack_drawing:
        if line == NEW_LINE:
            line_is_instruction = True
            CrateMover_9000.reverse_stacks()
            CrateMover_9001.reverse_stacks()
            continue
        if line_is_instruction:
            line_split = line.split(DELIMITER)
            n_crates = int(line_split[1])
            source_stack = int(line_split[3])
            target_stack = int(line_split[5])
            CrateMover_9000.move_crates_9000(n_crates, source_stack, target_stack)
            CrateMover_9001.move_crates_9001(n_crates, source_stack, target_stack)
        else:
            CrateMover_9000.parse_crates(line)
            CrateMover_9001.parse_crates(line)

    top_crates_9000 = ""
    top_crates_9001 = ""
    for crate_stack_9000, crate_stack_9001 in zip(
        CrateMover_9000.crate_stacks.values(), CrateMover_9001.crate_stacks.values()
    ):
        top_crates_9000 += crate_stack_9000[-1]
        top_crates_9001 += crate_stack_9001[-1]
    print(f"CrateMover 9000: {top_crates_9000}")
    print(f"CrateMover 9001: {top_crates_9001}")
