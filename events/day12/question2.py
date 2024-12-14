import time
from events.day12.question1 import Garden
from utils.network import get_input
from utils.objects import Grid, GridPoint


def count_sides(coords: GridPoint):
    sorted_coords = sorted(coords)
    side_count = 0

    for i in range(len(sorted_coords)):
        current = sorted_coords[i]
        next_coord = sorted_coords[(i + 1) % len(sorted_coords)]

        if is_edge(current, next_coord):
            side_count += 1

    return side_count


def is_edge(coord1, coord2):
    return coord1.x == coord2.x or coord1.y == coord2.y


def main(raw_input: str):
    grid = Grid(raw_input)
    visited = set()
    answer = 0
    for point in grid:
        if point in visited:
            continue
        garden = Garden(grid, point)
        print(count_sides(garden.plots))
        visited.update(garden.plots)

    return answer


if __name__ == "__main__":
    # raw_input = get_input(12, 2024)
    raw_input = """AAAA
BBCD
BBCC
EEEC
"""
    start = time.perf_counter()
    answer = main(raw_input)
    end = time.perf_counter()

    print(f"Question 2: {answer} in {(end - start) * 1000:.2f} ms")
