import time
from utils.network import get_input
from utils.objects import Grid, GridPoint


class Garden:
    def __init__(self, grid: Grid, point: GridPoint):
        self.grid = grid
        self.plots = {point}
        self.id = grid.get(point)
        self.perimiter: int = 4

        # Fill the garden
        self.flood_fill(point)


    def add_plot(self, plot: GridPoint):
        if plot not in self.plots:
            self.plots.add(plot)
            perimiter = 4
            for neighbor in self.grid.neighbors(plot):
                if neighbor in self.plots:
                    perimiter -= 2
            self.perimiter += perimiter


    def flood_fill(self, plot: GridPoint):
        for neighbor in self.grid.neighbors(plot):
            if self.grid.get(neighbor) == self.id and neighbor not in self.plots:
                self.add_plot(neighbor)
                self.flood_fill(neighbor)


    def price(self):
        return len(self.plots)*self.perimiter



def main(raw_input: str):
    grid = Grid(raw_input)
    visited = set()
    answer = 0
    for point in grid:
        if point in visited:
            continue
        garden = Garden(grid,point)
        answer += garden.price()
        visited.update(garden.plots)

    return answer


if __name__ == "__main__":
    raw_input = get_input(12, 2024)
    start = time.perf_counter()
    answer = main(raw_input)
    end = time.perf_counter()

    print(f"Question 1: {answer} in {(end - start) * 1000:.2f} ms")
