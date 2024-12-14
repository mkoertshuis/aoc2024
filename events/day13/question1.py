import time
from utils.network import get_input
from utils.parser import split_input
import re


def solve_puzzel(puzzel: str, tolerance=0.0001, offset: int = 0):
    ax, ay, bx, by, x, y = map(int, re.findall(r"(\d+)", puzzel))
    x, y = x + offset, y + offset
    A = (bx * y - by * x) / (bx * ay - by * ax)
    B = (x - ax * A) / bx
    if abs(A - round(A)) < tolerance and abs(B - round(B)) < tolerance:
        return int(3 * A + B)
    return 0


def parse(raw_input: str):
    return split_input(raw_input, "\n\n")


def main(raw_input: str):
    return sum(solve_puzzel(puzzel) for puzzel in parse(raw_input))


if __name__ == "__main__":
    raw_input = get_input(13, 2024)
    start = time.perf_counter()
    answer = main(raw_input)
    end = time.perf_counter()

    print(f"Question 1: {answer} in {(end - start) * 1000:.2f} ms")
