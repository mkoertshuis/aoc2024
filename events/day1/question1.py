from utils.network import get_input
from utils.parser import split_input
import numpy as np


def parse(_input):
    arr = np.array([split_input(a, "   ") for a in split_input(_input)])
    return arr.astype(int)


def sort_arrays(arr):
    return np.sort(arr, axis=0)


def get_distance(arr):
    new_arr = np.apply_along_axis(lambda x: np.abs(x[0]-x[1]), axis=-1, arr=arr)
    return new_arr.sum(axis=-1)


if __name__ == '__main__':
    raw_input = get_input(1, 2024)
    print("Question1:",get_distance(sort_arrays(parse(raw_input))))
