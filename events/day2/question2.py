from datetime import datetime
from events.day2.question1 import parse, sum_safe
from utils.network import get_input


if __name__ == "__main__":
    raw_input = get_input(2, 2024)
    arr = parse(raw_input)
    start = datetime.now()
    answer = sum_safe(arr, 1)
    end = datetime.now()

    print(f"Question 2: {answer} in {(end-start).microseconds} ms")
