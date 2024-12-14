import time
from utils.network import get_input


def main(raw_input: str):
    return 0


if __name__ == "__main__":
    raw_input = get_input(12, 2024)
    start = time.perf_counter()
    answer = main(raw_input)
    end = time.perf_counter()

    print(f"Question 2: {answer} in {(end - start) * 1000:.2f} ms")
