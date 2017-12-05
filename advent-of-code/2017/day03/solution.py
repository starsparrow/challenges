#!/usr/bin/env python

from sys import argv

memory_location = int(argv[1])


def make_grid(max_value):
    # Initialize
    grid = [(0, 0)]
    direction = 'E' 
    position = grid[0]
    min_row = 0
    max_row = 0
    min_col = 0
    max_col = 0

    while len(grid) < max_value:
        if direction == 'E':
            while position[0] <= max_col:
                position = (position[0] + 1, position[1])
                grid.append(position)
            max_col = position[0]
            direction = 'N'
        elif direction == 'N':
            while position[1] <= max_row:
                position = (position[0], position[1] + 1)
                grid.append(position)
            max_row = position[1]
            direction = 'W'
        elif direction == 'W':
            while position[0] >= min_col:
                position = (position[0] - 1, position[1])
                grid.append(position)
            min_col = position[0]
            direction = 'S'
        elif direction == 'S':
            while position[1] >= min_row:
                position = (position[0], position[1] - 1)
                grid.append(position)
            min_row = position[1]
            direction = 'E'
        
    return grid


def manhattan_distance(grid):
    return abs(grid[memory_location - 1][0]) + abs(grid[memory_location - 1][1])


grid = make_grid(memory_location)
print(manhattan_distance(grid))

