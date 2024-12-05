import time
from utils.network import get_input
from utils.parser import split_input
import numpy as np
import collections
import functools


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


@functools.cache
def check_order(a: int, rule: tuple[int]) -> bool:
    return a in rule


def check_update(update: np.ndarray[int], rules: collections.defaultdict):
    for idx, i in enumerate(update):
        rule = tuple(rules[i])
        for j in update[idx:]:
            if not check_order(j, rule):
                return False
    return True


def main(raw_input: str):
    rules, updates = parse(raw_input)
    correct = []
    for update in updates:
        if check_update(update,rules):
            middle = int(len(update) // 2)
            correct.append(update[middle])
    return sum(correct)



if __name__ == "__main__":
    # raw_input = get_input(5, 2024)
    raw_input = """47|53
97|13
97|61
97|47
75|29
61|13
75|53
29|13
97|29
53|29
61|53
97|53
61|29
47|13
75|47
97|75
47|61
75|61
47|29
75|13
53|13

75,47,61,53,29
97,61,53,29,13
75,29,13
75,97,47,61,53
61,13,29
97,13,75,29,47
"""
    start = time.perf_counter()
    answer = main(raw_input)
    end = time.perf_counter()

    print(f"Question 1: {answer} in {(end-start)*1000:.2f} ms")
