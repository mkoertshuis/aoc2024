import numpy as np

from utils.parser import split_input

DIRECTIONS = [(0, 1), (1, 0), (0, -1), (-1, 0)]

class GridPoint:
    def __init__(self,x,y):
        self.x = x
        self.y = y


    def __eq__(self, other):
        if isinstance(other, GridPoint):
            return self.x == other.x and self.y == other.y
        return False


    def __hash__(self):
        return hash((self.x, self.y))  # Hash based on the coordinates (x, y)


    def __repr__(self):
        return f"GridPoint({self.x}, {self.y})"


class Grid:
    def __init__(self,raw_input: str,dtype=str):
        self.arr = np.array([list(x) for x in split_input(raw_input)],dtype=dtype)
        self.shape = self.arr.shape
        self.width = self.shape[1]
        self.height = self.shape[0]
        self.current_x = 0
        self.current_y = 0

    def get(self,point: GridPoint):
        return self.arr[point.y][point.x]


    def neighbors(self, point: GridPoint):
        return [
            GridPoint(point.x+dx,point.y+dy)
            for dx, dy in DIRECTIONS
            if 0 <= point.x+dx < self.arr.shape[1]
            and 0 <= point.y+dy < self.arr.shape[0]
        ]


    def __iter__(self):
        self.current_x = 0
        self.current_y = 0
        return self


    def __next__(self):
        if self.current_y >= self.height:
            raise StopIteration
        point = GridPoint(self.current_x, self.current_y)
        self.current_x += 1
        if self.current_x >= self.width:
            self.current_x = 0
            self.current_y += 1
        return point
