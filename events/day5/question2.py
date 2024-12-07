import time
from utils.network import get_input
from events.day5.question1 import parse, check_update
import numpy as np


def order_update(update,rules):
    ordered_lst = np.array(update)
    while True:
        vld, vld_i, inp_i = check_update(ordered_lst,rules)
        if vld:
            break
        ordered_lst = np.concatenate((
            ordered_lst[:vld_i],
            [ordered_lst[inp_i]],
            ordered_lst[vld_i:inp_i],
            ordered_lst[inp_i+1:]
        ))
    return ordered_lst


def main(raw_input: str):
    rules, updates = parse(raw_input)
    incorrect = []
    for update in updates:
        if not check_update(update,rules)[0]:
            ordered_update = order_update(update,rules)
            middle = int(len(ordered_update) // 2)
            incorrect.append(int(ordered_update[middle]))
            break
    return sum(incorrect)



if __name__ == "__main__":
    raw_input = get_input(5, 2024)
    start = time.perf_counter()
    answer = main(raw_input)
    end = time.perf_counter()

    print(f"Question 1: {answer} in {(end-start)*1000:.2f} ms")
