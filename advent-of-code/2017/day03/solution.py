#!/usr/bin/env python

from sys import argv

memory_location = int(argv[1])


def make_sequential_grid(max_value):
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


def get_adjacent_sum_grid(penultimate_value):
    # Initialize
    grid = [(0, 0)]
    grid_values = {(0, 0): 1}
    max_value = 1
    direction = 'E' 
    position = grid[0]
    min_row = 0
    max_row = 0
    min_col = 0
    max_col = 0

    def get_adjacent_sums(current_position):
        surrounding_square_map = [(1,0), (1,-1), (0,-1), (-1,-1), (-1,0), (-1,1), (0,1), (1,1)]
        surrounding_squares = [tuple(map(sum, zip(current_position, surrounding_square))) for surrounding_square in surrounding_square_map]
        surrounding_values = [grid_values.get(square) if square in grid else 0 for square in surrounding_squares]
        surrounding_values_sum = sum([value if value is not None else 0 for value in surrounding_values])
        grid_values[current_position] = surrounding_values_sum 
        return surrounding_values_sum

    while sorted(grid_values.values())[-1] < penultimate_value:
        if direction == 'E':
            while position[0] <= max_col:
                position = (position[0] + 1, position[1])
                grid.append(position)
                adjacent_sum = get_adjacent_sums(grid[-1])
                max_value = adjacent_sum if max_value < adjacent_sum else max_value
            max_col = position[0]
            direction = 'N'
        elif direction == 'N':
            while position[1] <= max_row:
                position = (position[0], position[1] + 1)
                grid.append(position)
                adjacent_sum = get_adjacent_sums(grid[-1])
                max_value = adjacent_sum if max_value < adjacent_sum else max_value
            max_row = position[1]
            direction = 'W'
        elif direction == 'W':
            while position[0] >= min_col:
                position = (position[0] - 1, position[1])
                grid.append(position)
                adjacent_sum = get_adjacent_sums(grid[-1])
                max_value = adjacent_sum if max_value < adjacent_sum else max_value
            min_col = position[0]
            direction = 'S'
        elif direction == 'S':
            while position[1] >= min_row:
                position = (position[0], position[1] - 1)
                grid.append(position)
                adjacent_sum = get_adjacent_sums(grid[-1])
                max_value = adjacent_sum if max_value < adjacent_sum else max_value
            min_row = position[1]
            direction = 'E'
        
    return [value for value in sorted(grid_values.values()) if value > penultimate_value][0]


def manhattan_distance(grid):
    return abs(grid[memory_location - 1][0]) + abs(grid[memory_location - 1][1])


grid1 = make_sequential_grid(memory_location)
print(manhattan_distance(grid1))

print(get_adjacent_sum_grid(memory_location))

