import time
from events.day8.question1 import find_antinodes, parse
from utils.network import get_input


def main(raw_input: str):
    arr = parse(raw_input)
    return len(find_antinodes(arr, True))


if __name__ == "__main__":
    raw_input = get_input(8, 2024)
    start = time.perf_counter()
    answer = main(raw_input)
    end = time.perf_counter()

    print(f"Question 2: {answer} in {(end - start) * 1000:.2f} ms")
