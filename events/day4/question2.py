import time
from utils.network import get_input
from utils.parser import split_input

DIRECTIONS = [
    # Only two directions needed because they are just mirrored
    ((1, 1), (-1, -1)),
    ((-1, 1), (1, -1)),
]


def find_words(arr: list[str], x: int, y: int):
    """Check if a potential intersection contains bot MAS diagonals"""
    answer = 0
    for (x0, y0), (x1, y1) in DIRECTIONS:
        try:
            # No turn-over
            if x + x0 < 0 or x + x1 < 0 or y + y0 < 0 or y + y1 < 0:
                return 0
            # Find diagonal
            if set(arr[x + x0][y + y0] + arr[x + x1][y + y1]) == set("MS"):
                answer += 1
        except IndexError:
            continue
    # Need two diagonals so check if we found both
    return 1 if answer == 2 else 0


def main(raw_input: str):
    arr = split_input(raw_input)
    answer = 0
    for x, i in enumerate(arr):
        for y, j in enumerate(i):
            # Find potential intersection
            if j == "A":
                answer += find_words(arr, x, y)
    return answer


if __name__ == "__main__":
    raw_input = get_input(4, 2024)
    start = time.perf_counter()
    answer = main(raw_input)
    end = time.perf_counter()

    print(f"Question 2: {answer} in {(end-start)*1000:.2f} ms")
