from argparse import ArgumentParser
from pathlib import Path
from typing import List
import numpy as np

argument_parser = ArgumentParser()
argument_parser.add_argument(
    "--input",
    help="Input to file containing calorie data.",
    type=Path,
    required=True,
)
parsed_args = argument_parser.parse_args()

DELIMITER = "\n"


def get_snack_items(input_file_path: Path) -> List[str]:
    with open(input_file_path, "r") as input_file:
        snack_items = input_file.readlines()
    return snack_items


def print_results(top_elves_indices: List[int], elf_calorie_counts: np.array):
    top3_elves_result = "- In no particular order -\n"
    for elf_idx in top_elves_indices:
        top3_elves_result += f"Elf #{elf_idx+1}: {elf_calorie_counts[elf_idx]}\n"
    top3_elves_result += f"Total calorie count of "
    top3_elves_result += f"{np.sum(elf_calorie_counts[top_elves_indices])} kcal."
    print(top3_elves_result)


if __name__ == "__main__":
    snack_items = get_snack_items(parsed_args.input)
    n_elves = snack_items.count(DELIMITER) + 1
    elf_calorie_counts: np.array = np.zeros(dtype=int, shape=(n_elves,))

    elf_idx = 0
    for snack in snack_items:
        if snack == DELIMITER:
            elf_idx += 1
        else:
            elf_calorie_counts[elf_idx] += int(snack)

    # O(n) - linear time complexity
    top3_elves_indices = np.argpartition(elf_calorie_counts, -3)[-3:]

    print_results(top3_elves_indices, elf_calorie_counts)
