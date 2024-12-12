from itertools import product
import time
from utils.network import get_input
from utils.parser import split_input
import numpy as np


def add(a: int, b: int) -> int:
    return int(a) + int(b)


def mul(a: int, b: int) -> int:
    return int(a) * int(b)


def parse(raw_input: str):
    arr = np.array([split_input(x, ":") for x in split_input(raw_input)])
    values = arr[:, 0]
    equations = [split_input(x, " ") for x in arr[:, 1]]
    return values, equations


def calculate(equation, value, operands):
    strategies = product(operands, repeat=len(equation) - 1)
    for strategy in strategies:
        queue = iter(equation)
        register = next(queue)
        for operation in strategy:
            register = operation(register, next(queue))
        if register == int(value):
            return True
    return False


def main(raw_input: str):
    values, equations = parse(raw_input)
    answer = 0
    for value, equation in zip(values, equations):
        if calculate(equation, value, (add, mul)):
            answer += int(value)
    return answer


if __name__ == "__main__":
    raw_input = get_input(7, 2024)
    start = time.perf_counter()
    answer = main(raw_input)
    end = time.perf_counter()

    print(f"Question 1: {answer} in {(end - start) * 1000:.2f} ms")
