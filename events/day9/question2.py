import time
from itertools import chain
from events.day9.question1 import checksum, pairwise
import copy

from utils.network import get_input


def fill_disk(raw_input: str) -> list:
    # Pad if necessary
    if len(raw_input) % 2 != 0:
        raw_input += " "
    # Fill disk
    disk = []
    for idx, (fill, empty) in enumerate(pairwise(raw_input)):
        disk.append([idx] * int(fill))
        if empty != " ":
            disk.append([None] * int(empty))

    return list(filter(lambda b: b, disk))


def compress(disk: list) -> list:
    result = copy.deepcopy(disk)
    while disk:
        file = disk.pop()
        for idx, partition in enumerate(result[:len(disk)]):
            if partition[0] is None and len(partition) >= len(file):
                # Move the file to this partition
                result[idx] = file
                # Remove moved space with None
                for j, block in enumerate(result[idx+1:],idx+1):
                    if block == file:
                        result[j] = [None] * len(file)
                        break
                # Handle leftover empty space
                if len(partition) > len(file):
                    result.insert(idx + 1, [None] * (len(partition) - len(file)))
                break

    # Combine result and tail
    return result


def main(raw_input: str):
    disk = fill_disk(raw_input)
    compressed = compress(disk)
    flattened = list(chain.from_iterable(compressed))
    print(flattened)
    return checksum(flattened)


if __name__ == "__main__":
    raw_input = get_input(9, 2024).replace("\n","")
    start = time.perf_counter()
    answer = main(raw_input)
    end = time.perf_counter()

    print(f"Question 2: {answer} in {(end - start) * 1000:.2f} ms")

    # x < 6442064707697
