from utils.network import get_input
from utils.parser import split_input
import numpy as np


def parse(raw_input: str) -> list[np.ndarray[int]]:
    return [
        np.array(split_input(line, " "), dtype=int) for line in split_input(raw_input)
    ]


def check_safe(levels: np.ndarray[int], error: int = 0) -> int:
    levels_diff = np.diff(levels)

    if np.all((levels_diff > 0) & (levels_diff <= 3)):
        return 1
    if np.all((levels_diff < 0) & (levels_diff >= -3)):
        return 1

    if error > 0:
        for i in range(len(levels)):
            levels_with_one_removed = np.delete(levels, i)
            if check_safe(levels_with_one_removed, error - 1) == 1:
                return 1

    return 0


def sum_safe(arr: list[np.ndarray[int]], error: int = 0) -> int:
    return sum(check_safe(levels, error) for levels in arr)


if __name__ == "__main__":
    raw_input = get_input(2, 2024)
    arr = parse(raw_input)
    print("Question 1:", sum_safe(arr))
