import time
from utils.network import get_input
from collections import deque
import math


def pairwise(s):
    for i in range(0, len(s), 2):
        yield s[i : i + 2]


def fill_disk(raw_input: str) -> list:
    # Pad if necessary
    if len(raw_input) % 2 != 0:
        raw_input += " "
    # Fill disk
    disk = []
    for idx, (fill, empty) in enumerate(pairwise(raw_input)):
        disk += [idx] * int(fill)
        if empty != " ":
            disk += [None] * int(empty)

    return disk


def compress(disk: str) -> list:
    disk = deque(disk)
    compressed = []
    while disk:
        v = disk.popleft()
        if v is None:
            w = None
            while disk and w is None:
                w = disk.pop()
            compressed += [w]
        else:
            compressed += [v]
    return compressed


def checksum(compressed: str):
    return sum(math.prod([a, int(b)]) for a, b in enumerate(compressed) if b)


def main(raw_input: str):
    disk = fill_disk(raw_input)
    compressed = compress(disk)
    return checksum(compressed)


if __name__ == "__main__":
    raw_input = get_input(9, 2024).replace("\n", "")
    start = time.perf_counter()
    answer = main(raw_input)
    end = time.perf_counter()

    print(f"Question 1: {answer} in {(end - start) * 1000:.2f} ms")
