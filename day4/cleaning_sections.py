from argparse import ArgumentParser
from pathlib import Path
from typing import List
import numpy as np

argument_parser = ArgumentParser()
argument_parser.add_argument(
    "--input",
    help="Input to cleaning schedule.",
    type=Path,
    required=True,
)
parsed_args = argument_parser.parse_args()

ELF_DELIMITER = ","
SECTION_DELIMITER = "-"


def get_schedule(input_file_path: Path) -> List[str]:
    with open(input_file_path, "r") as input_file:
        elf_pairs = input_file.readlines()
    return elf_pairs


def overlapping_schedule_part1(elf1_range: List[int], elf2_range: List[int]) -> bool:
    elf2_range_list = range(elf2_range[0], elf2_range[1]+1)
    elf1_range_list = range(elf1_range[0], elf1_range[1]+1)
    elf1_schedule_in_elf2 = all(
        section in elf2_range_list for section in elf1_range)
    elf2_schedule_in_elf1 = all(
        section in elf1_range_list for section in elf2_range)
    if elf1_schedule_in_elf2 or elf2_schedule_in_elf1:
        return True
    return False


def overlapping_schedule_part2(elf1_range: List[int], elf2_range: List[int]) -> bool:
    elf1_range_list = range(elf1_range[0], elf1_range[1]+1)
    elf2_range_list = range(elf2_range[0], elf2_range[1]+1)
    return bool(set(elf1_range_list) & set(elf2_range_list))


if __name__ == "__main__":
    elf_pairs = get_schedule(parsed_args.input)
    n_overlapping_schedules_part1 = 0
    n_overlapping_schedules_part2 = 0
    for elf_pair in elf_pairs:
        elf1, elf2 = elf_pair.split(ELF_DELIMITER)

        elf1_range = [int(i) for i in elf1.split(SECTION_DELIMITER)]
        elf2_range = [int(i) for i in elf2.split(SECTION_DELIMITER)]

        if overlapping_schedule_part1(elf1_range, elf2_range):
            n_overlapping_schedules_part1 += 1

        if overlapping_schedule_part2(elf1_range, elf2_range):
            n_overlapping_schedules_part2 += 1

    print(f"Part 1: {n_overlapping_schedules_part1}")
    print(f"Part 2: {n_overlapping_schedules_part2}")
