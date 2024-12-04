import time
from utils.network import get_input
from utils.parser import split_input


WORD = "XMAS"
DIRECTIONS = [(0, 1), (1, 0), (1, 1), (0, -1), (-1, 0), (-1, -1), (1, -1), (-1, 1)]


def find_word(arr: list[str], x: int, y: int, dx: int, dy: int, word: str):
    """Recursive find the complete word"""
    if word != WORD[: len(word)]:
        return 0
    try:
        new_x = x + dx
        new_y = y + dy
        if new_x >= 0 and new_y >= 0:  # Out of index
            word += arr[x + dx][y + dy]
        else:
            return 0
    except IndexError:
        return 0

    if word == WORD:
        return 1

    return find_word(arr, x + dx, y + dy, dx, dy, word)


def main(raw_input: str):
    arr = split_input(raw_input)
    answer = 0
    for x, i in enumerate(arr):
        for y, j in enumerate(i):
            if j == WORD[0]:
                answer += sum(find_word(arr, x, y, dx, dy, j) for dx, dy in DIRECTIONS)
    return answer


if __name__ == "__main__":
    raw_input = get_input(4, 2024)
    start = time.perf_counter()
    answer = main(raw_input)
    end = time.perf_counter()

    print(f"Question 1: {answer} in {(end-start)*1000:.2f} ms")
