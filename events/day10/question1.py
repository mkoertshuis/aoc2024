import time
import numpy as np
from utils.network import get_input
from utils.parser import split_input


directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]


def score_trailhead(arr, x, y) -> int:
    score = 0
    visited = set()

    queue = [(x, y)]

    while queue:
        cur = queue.pop()

        if cur in visited:
            continue

        visited.add(cur)

        if (val := arr[cur[1]][cur[0]]) == 9:
            score += 1
            continue

        queue.extend(
            (cur[0] + dx, cur[1] + dy)
            for dx, dy in directions
            if 0 <= cur[0] + dx < arr.shape[1]
            and 0 <= cur[1] + dy < arr.shape[0]
            and arr[cur[1] + dy][cur[0] + dx] == val + 1
        )

    return score


def parse(raw_input: str):
    return np.array(
        [list(map(int, line.strip())) for line in split_input(raw_input)], dtype=int
    )


def main(raw_input: str):
    arr = parse(raw_input)
    zeros = np.where(arr == 0)
    answer = 0

    for x, y in zip(zeros[1], zeros[0]):
        answer += score_trailhead(arr, x, y)

    return answer


if __name__ == "__main__":
    raw_input = get_input(10, 2024)
    start = time.perf_counter()
    answer = main(raw_input)
    end = time.perf_counter()

    print(f"Question 1: {answer} in {(end - start) * 1000:.2f} ms")
