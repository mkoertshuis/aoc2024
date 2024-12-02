from utils.network import get_input
from utils.parser import split_input
import numpy as np

def check_safe(line: str):
    levels = np.array(split_input(line," "),dtype=int)
    levels_diff = np.diff(levels)

    if np.all((levels_diff > 0) & (levels_diff <= 3)):
        return 1
    if np.all((levels_diff < 0) & (levels_diff >= -3)):
        return 1

    return 0

def sum_safe(arr: list[str]):
    return sum(check_safe(line) for line in arr)

if __name__ == '__main__':
    raw_input = get_input(2,2024)
    arr = split_input(raw_input)
    print("Question 1:", sum_safe(arr))
