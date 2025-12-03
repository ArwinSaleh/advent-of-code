from argparse import ArgumentParser
from pathlib import Path
from typing import List
import numpy as np

argument_parser = ArgumentParser()
argument_parser.add_argument(
    "--input",
    help="Input to file containing RPS strategy.",
    type=Path,
    required=True,
)
parsed_args = argument_parser.parse_args()

DELIMITER = " "

RPS_RULES = {
    'X': {
        "points": 1,
        "takes": 'C',
        "responses": {
            'A': 'Z',
            'B': 'X',
            'C': 'Y',
            "points": 0,
        },
    },
    'Y': {
        "points": 2,
        "takes": 'A',
        "responses": {
            'A': 'X',
            'B': 'Y',
            'C': 'Z',
            "points": 3,
        },
    },
    'Z': {
        "points": 3,
        "takes": 'B',
        "responses": {
            'A': 'Y',
            'B': 'Z',
            'C': 'X',
            "points": 6,
        },
    },
}
RPS_MAP = {
    'X': 'A',
    'Y': 'B',
    'Z': 'C',
}


def get_rps_rounds(input_file_path: Path) -> List[str]:
    with open(input_file_path, "r") as input_file:
        rps_rounds = input_file.readlines()
    return rps_rounds


def run_rps():
    rps_rounds: List[str] = get_rps_rounds(parsed_args.input)
    n_rounds: int = len(rps_rounds)
    all_results_part1: np.array = np.zeros(dtype=int, shape=(n_rounds,))
    all_results_part2: np.array = np.zeros(dtype=int, shape=(n_rounds,))

    for round_idx in range(n_rounds):
        [opponent, strategy] = rps_rounds[round_idx].strip().split(DELIMITER)

        # Part 1
        round_score = RPS_RULES[strategy]["points"]
        if opponent == RPS_MAP[strategy]:
            round_score += 3
        elif opponent == RPS_RULES[strategy]["takes"]:
            round_score += 6
        all_results_part1[round_idx] = round_score

        # Part2
        round_score = RPS_RULES[strategy]["responses"]["points"]
        strategy_outcome = RPS_RULES[strategy]["responses"][opponent]
        round_score += RPS_RULES[strategy_outcome]["points"]
        all_results_part2[round_idx] = round_score

    total_score = np.sum(all_results_part1)
    print(f"Total score with strategy 1: {total_score}")

    total_score = np.sum(all_results_part2)
    print(f"Total score with strategy 2: {total_score}")


if __name__ == "__main__":
    run_rps()
