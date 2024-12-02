import time
import numpy as np
from events.day1.question1 import parse
from utils.network import get_input


def calculate_similarity(arr):
    V, C = np.array(np.unique(arr[:, 0], return_counts=True))
    VV, CC = np.unique(arr[:, 1], return_counts=True)
    dictionary = dict(zip(VV, CC))

    similarity = sum(v * dictionary.get(v, 0) * c for v, c in zip(V, C))

    return int(similarity)


if __name__ == "__main__":
    raw_input = get_input(1, 2024)
    arr = parse(raw_input)
    start = time.perf_counter()
    answer = calculate_similarity(arr)
    end = time.perf_counter()

    print(f"Question 2: {answer} in {(end-start)*1000:.2f} ms")
