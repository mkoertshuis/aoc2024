import time
from utils.network import get_input
from utils.parser import split_input
from collections import deque
import numpy as np


def parse(raw_input: str):
    return np.array([list(x) for x in split_input(raw_input, "\n")])


def get_location(arr):
    indices = np.where(arr == "^")
    return int(indices[1][0]), int(indices[0][0])


def walk(arr):
    d = deque([(0, -1), (1, 0), (0, 1), (-1, 0)])
    current_location = get_location(arr)
    locations = set([current_location])  # Initialize with current location
    x_lim, y_lim = arr.shape

    while True:
        dx, dy = d[0]
        new_location = (current_location[0] + dx, current_location[1] + dy)

        # Check bounds first
        if not (0 <= new_location[0] < x_lim and 0 <= new_location[1] < y_lim):
            break

        # Check for wall
        if arr[new_location[1]][new_location[0]] == "#":
            d.rotate(-1)  # next direction
            continue

        # Update the current location
        locations.add(new_location)
        current_location = new_location

    return len(locations)


def main(raw_input: str):
    arr = parse(raw_input)
    return walk(arr)


if __name__ == "__main__":
    raw_input = get_input(6, 2024)
    start = time.perf_counter()
    answer = main(raw_input)
    end = time.perf_counter()

    print(f"Question 1: {answer} in {(end - start) * 1000:.2f} ms")
