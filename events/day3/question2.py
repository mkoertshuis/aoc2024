import time
from events.day3.question1 import calculate, get_instructions
from utils.network import get_input
import re


def filter_input(raw_input: str) -> str:
    """
    Find all the "do" instructions.txt

    Basicly find all the do() ... don't() or EOF
    and beware of the possibility of do() instructions
    inside do() instructions.
    """
    expr = r"(do\(\)(?:.*?)(?:don't\(\)|$))"  # Uses end of string so beware of \n inside the input
    pattern = re.compile(expr)

    matches = [
        match.group(0)
        for match in pattern.finditer("do()" + raw_input.replace("\n", ""))
    ]

    return "".join(matches)


def main(raw_input: str) -> int:
    """Main function of day 3 question 2"""
    filtered = filter_input(raw_input)  # Filter out all the don't() instructions
    return calculate(get_instructions(filtered))  # Same as question 1


if __name__ == "__main__":
    raw_input = get_input(3, 2024)
    start = time.perf_counter()
    answer = main(raw_input)
    end = time.perf_counter()

    print(f"Question 2: {answer} in {(end-start)*1000:.2f} ms")
