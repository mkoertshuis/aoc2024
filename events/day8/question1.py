import time
from utils.network import get_input
from utils.parser import split_input
import numpy as np
from itertools import combinations


def parse(raw_input):
    """Not necessary to parse the lines, but I find it clear"""
    return np.array([list(x) for x in split_input(raw_input)])


def find_antinodes(arr, harmonics=False):
    unique = np.unique(arr)
    unique = unique[unique != "."]  # Exclude empty cells
    answer = set()
    row_lim, col_lim = arr.shape

    for antenna in unique:
        coords = np.array(np.where(arr == antenna)).T
        for antenna0, antenna1 in combinations(coords, 2):
            d_row, d_col = antenna1 - antenna0

            if harmonics:
                for step in range(1, max(row_lim, col_lim)):
                    antinode = antenna1 - step * np.array([d_row, d_col])
                    if 0 <= antinode[0] < row_lim and 0 <= antinode[1] < col_lim:
                        answer.add(tuple(antinode))
                    else:
                        break

                for step in range(1, max(row_lim, col_lim)):
                    antinode = antenna0 + step * np.array([d_row, d_col])
                    if 0 <= antinode[0] < row_lim and 0 <= antinode[1] < col_lim:
                        answer.add(tuple(antinode))
                    else:
                        break

            else:
                antinodes = [antenna0 - [d_row, d_col], antenna1 + [d_row, d_col]]
                for antinode in antinodes:
                    if 0 <= antinode[0] < row_lim and 0 <= antinode[1] < col_lim:
                        answer.add(tuple(antinode))

    return answer


def main(raw_input: str):
    arr = parse(raw_input)
    return len(find_antinodes(arr))


if __name__ == "__main__":
    raw_input = get_input(8, 2024)
    start = time.perf_counter()
    answer = main(raw_input)
    end = time.perf_counter()

    print(f"Question 1: {answer} in {(end - start) * 1000:.2f} ms")
