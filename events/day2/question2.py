import numpy as np
from utils.network import get_input
from utils.parser import split_input

def check_safe_dampener(line: str, error: int = 1):
    levels = np.array(split_input(line, " "), dtype=int)
    levels_diff = np.diff(levels)

    if np.all((levels_diff > 0) & (levels_diff <= 3)):
        return 1
    if np.all((levels_diff < 0) & (levels_diff >= -3)):
        return 1

    pos_out_of_range = (levels_diff <= 0) | (levels_diff > 3)
    if np.sum(pos_out_of_range) <= error:
        valid_levels = np.delete(levels, np.where(pos_out_of_range)[0]+1)
        new_diff = np.diff(valid_levels)
        if np.all((new_diff > 0) & (new_diff <= 3)):
            return 1

    neg_out_of_range = (levels_diff >= 0) | (levels_diff < -3)
    if np.sum(neg_out_of_range) <= error:
        valid_levels = np.delete(levels, np.where(neg_out_of_range)[0]+1)
        new_diff = np.diff(valid_levels)
        if np.all((new_diff < 0) & (new_diff >= -3)):
            return 1

    return 0

def sum_safe_dampener(arr: list[str]):
    return sum(check_safe_dampener(line) for line in arr)

if __name__ == '__main__':
    raw_input = get_input(2,2024)
    arr = split_input(raw_input)
    print("Question 2:", sum_safe_dampener(arr))