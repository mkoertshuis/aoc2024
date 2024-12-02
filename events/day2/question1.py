from datetime import datetime
from utils.network import get_input
from utils.parser import split_input
import numpy as np


def parse(raw_input: str) -> list[np.ndarray[int]]:
    """Create a list of ndarrays to make using numpy easier"""
    return [
        np.array(split_input(line, " "), dtype=int) for line in split_input(raw_input)
    ]


def check_safe(levels: np.ndarray[int], error: int = 0) -> int:
    """Check if the levels are safe"""
    levels_diff = np.diff(levels)

    if np.all((levels_diff > 0) & (levels_diff <= 3)):
        return 1
    if np.all((levels_diff < 0) & (levels_diff >= -3)):
        return 1

    # Needed for question 2
    if error > 0:
        # Little bit of a bruteforce, would be better to detect the error and
        # check safe if the error is removed
        for i in range(len(levels)):
            levels_with_one_removed = np.delete(levels, i)
            # Check recursive
            if check_safe(levels_with_one_removed, error - 1):
                return 1

    return 0


def sum_safe(arr: list[np.ndarray[int]], error: int = 0) -> int:
    """Sum all the safe levels"""
    return sum(check_safe(levels, error) for levels in arr)


if __name__ == "__main__":
    raw_input = get_input(2, 2024)
    arr = parse(raw_input)
    start = datetime.now()
    answer = sum_safe(arr)
    end = datetime.now()

    print(f"Question 1: {answer} in {(end-start).microseconds} ms")
