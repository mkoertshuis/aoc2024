import time
from utils.network import get_input
from utils.parser import split_input
import numpy as np
import collections


def parse(raw_input: str):
    raw_rules, updates = split_input(raw_input,"\n\n")

    raw_rules = split_input(raw_rules,"\n")
    rules = collections.defaultdict(list)
    for rule in raw_rules:
        k,v = split_input(rule,"|")
        rules[int(k)].append( int(v) )

    updates = [
        np.array(split_input(update,','),dtype=int)
        for update in split_input(updates)
    ]

    return rules, updates


def check_update(update: np.ndarray[int], rules: collections.defaultdict):
    for idx, i in enumerate(update):
        violations = np.in1d(update[:idx], rules[i])
        if np.any(violations):
            return False, np.where(violations)[0][0], idx
    return True, -1, -1


def main(raw_input: str):
    rules, updates = parse(raw_input)
    correct = []
    for update in updates:
        if check_update(update,rules)[0]:
            middle = int(len(update) // 2)
            correct.append(update[middle])
    return sum(correct)



if __name__ == "__main__":
    raw_input = get_input(5, 2024)
    start = time.perf_counter()
    answer = main(raw_input)
    end = time.perf_counter()

    print(f"Question 1: {answer} in {(end-start)*1000:.2f} ms")
