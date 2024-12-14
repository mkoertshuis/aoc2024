import time
from utils.network import get_input
from utils.parser import split_input
import functools


@functools.cache
def blink(stone: int, depth: int, max_depth: int):
    while depth < max_depth:
        if stone == 0:
            stone = 1
            depth += 1
            continue

        a_str = str(stone)
        if len(a_str) % 2 == 0:
            mask = 10 ** (len(a_str) // 2)
            left = stone // mask
            right = stone % mask
            return blink(left, depth + 1, max_depth) + blink(
                right, depth + 1, max_depth
            )

        stone *= 2024
        depth += 1
    return 1


def run(raw_input: str, n: int):
    lst = [int(x) for x in split_input(raw_input, " ")]
    return sum(blink(stone, 0, n) for stone in lst)


def main(raw_input: str):
    return run(raw_input, 25)


if __name__ == "__main__":
    raw_input = get_input(11, 2024)
    start = time.perf_counter()
    answer = main(raw_input)
    end = time.perf_counter()

    print(f"Question 1: {answer} in {(end - start) * 1000:.2f} ms")
