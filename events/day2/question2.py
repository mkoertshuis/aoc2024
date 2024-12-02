import time
from events.day2.question1 import parse, sum_safe
from utils.network import get_input

# Reuse everything from question 1 and
# only assign an error parameter to the sum_safe function

if __name__ == "__main__":
    raw_input = get_input(2, 2024)
    arr = parse(raw_input)
    start = time.perf_counter()
    answer = sum_safe(arr, 1)
    end = time.perf_counter()

    print(f"Question 2: {answer} in {(end-start)*1000:.2f} ms")
