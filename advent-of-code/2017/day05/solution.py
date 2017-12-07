#!/usr/bin/env python3

from sys import argv

with open(argv[1], 'r') as input_file:
    offsets = [int(line.strip()) for line in input_file.readlines()]

method = int(argv[2])

position = 0
jumps = 0

while True:
    try:
        next_position = position + offsets[position]
        if method == 1:
            offsets[position] += 1
        elif method == 2:
            if offsets[position] >= 3:
                offsets[position] -= 1
            else:
                offsets[position] += 1
        else:
            raise SystemExit('Invalid offset method')
        jumps += 1
        position = next_position
    except IndexError:
        print('Jumped off the list after {} jumps'.format(jumps))
        raise SystemExit()

