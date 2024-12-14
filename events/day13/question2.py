import time
from events.day13.question1 import parse, solve_puzzel
from utils.network import get_input


def main(raw_input: str):
    return sum(
        solve_puzzel(puzzel, 0.0001, 10000000000000) for puzzel in parse(raw_input)
    )


if __name__ == "__main__":
    raw_input = get_input(13, 2024)
    start = time.perf_counter()
    answer = main(raw_input)
    end = time.perf_counter()

    print(f"Question 2: {answer} in {(end - start) * 1000:.2f} ms")
