from events.day2.question1 import parse, sum_safe
from utils.network import get_input


if __name__ == "__main__":
    raw_input = get_input(2, 2024)
    arr = parse(raw_input)
    print("Question 2:", sum_safe(arr, 1))
