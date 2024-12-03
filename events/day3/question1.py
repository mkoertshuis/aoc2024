import time
from utils.network import get_input
import re


def get_instructions(raw_input: str) -> list[str]:
    """Find all the instructions of the input"""
    return re.findall(r"mul\([0-9]+,[0-9]+\)", raw_input)


def parse_instruction(instruction: str) -> int:
    """Parse the multiply functions"""
    x = re.search(r"[0-9]+,[0-9]+", instruction).group().split(",")
    return int(x[0]) * int(x[1])


def calculate(instructions: list[str]):
    """Sum all the instructions"""
    return sum(parse_instruction(instruction) for instruction in instructions)


def main(raw_input: str) -> int:
    """Main function of day 3 question 1"""
    return calculate(get_instructions(raw_input))


if __name__ == "__main__":
    raw_input = get_input(3, 2024)
    start = time.perf_counter()
    answer = main(raw_input)
    end = time.perf_counter()

    print(f"Question 1: {answer} in {(end-start)*1000:.2f} ms")
