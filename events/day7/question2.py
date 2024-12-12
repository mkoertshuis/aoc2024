import time
from events.day7.question1 import add, calculate, mul, parse
from utils.network import get_input


def concat(a: int, b: int) -> int: return int(f"{a}{b}")


def main(raw_input: str):
    values, equations = parse(raw_input)
    answer = 0
    for value, equation in zip(values, equations):
        if calculate(equation,value,(concat,add,mul)):
            answer += int(value)
    return answer


if __name__ == "__main__":
    raw_input = get_input(7, 2024)
    start = time.perf_counter()
    answer = main(raw_input)
    end = time.perf_counter()

    print(f"Question 1: {answer} in {(end - start) * 1000:.2f} ms")
