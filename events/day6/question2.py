from collections import deque
import time
from events.day6.question1 import get_location, parse
import numpy as np

from utils.network import get_input


def visualize_grid(arr, locations, obstructions):
    # Create a copy of the array to avoid modifying the original
    visualized_arr = arr
    
    # Mark traversed locations with 'X'
    for x, y in locations:
        if 0 <= x < visualized_arr.shape[1] and 0 <= y < visualized_arr.shape[0]:
            visualized_arr[y, x] = 'X'
    
    # Mark obstructions with 'O'
    for x, y in obstructions:
        if 0 <= x < visualized_arr.shape[1] and 0 <= y < visualized_arr.shape[0]:
            visualized_arr[y, x] = 'O'
    
    return visualized_arr


def check_loop(d, start_location, arr, obstruction) -> bool:
    """Check if a loop can be formed starting from a given location."""
    start_dir = d[0]
    locations = set([start_location])
    current_location = start_location
    x_lim, y_lim = arr.shape

    steps = 0
    max_steps = x_lim * y_lim

    while steps < max_steps:
        dx, dy = d[0]
        new_location = (current_location[0] + dx, current_location[1] + dy)

        # Check bounds
        if not (0 <= new_location[0] < x_lim and 0 <= new_location[1] < y_lim):
            return False

        # Check for walls or obstruction
        if arr[new_location[1]][new_location[0]] == "#" or new_location == obstruction:
            d.rotate(-1)  # Rotate to the next direction
            continue

        # Check if loop is completed
        if new_location == start_location and start_dir == d[0] and steps > 0:
            return True

        # Update state
        locations.add(new_location)
        current_location = new_location
        steps += 1

    return False

def walk(arr):
    """Traverse the grid and find all obstructions that can form loops."""
    d = deque([(0, -1), (1, 0), (0, 1), (-1, 0)])  # Directions: Up, Right, Down, Left
    current_location = get_location(arr)
    locations = set([current_location])
    x_lim, y_lim = arr.shape
    obstructions = set()

    while True:
        dx, dy = d[0]
        new_location = (current_location[0] + dx, current_location[1] + dy)

        # Check bounds
        if not (0 <= new_location[0] < x_lim and 0 <= new_location[1] < y_lim):
            break

        # Check for walls
        if arr[new_location[1]][new_location[0]] == "#":
            d.rotate(-1)  # Rotate to the next direction
            continue

        # Check if a loop can be created
        obstruction = (new_location[0] + dx, new_location[1] + dy)
        if (
            0 <= obstruction[0] < x_lim
            and 0 <= obstruction[1] < y_lim
            and arr[obstruction[1]][obstruction[0]] != "#"
            and obstruction not in obstructions
            and check_loop(deque(d), new_location, arr, obstruction)
        ):
            obstructions.add(obstruction)

        # Update the current location
        locations.add(new_location)
        current_location = new_location

    return len(obstructions)

def main(raw_input: str):
    """Parse input and compute the number of obstructions causing loops."""
    arr = parse(raw_input)
    return walk(arr)

if __name__ == "__main__":
    raw_input = get_input(6, 2024)
    start = time.perf_counter()
    answer = main(raw_input)
    end = time.perf_counter()

    print(f"Question 2: {answer} in {(end-start)*1000:.2f} ms")

    # 1422 < x < 1539
