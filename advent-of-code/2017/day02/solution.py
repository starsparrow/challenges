#!/usr/bin/env python

from sys import argv

with open('input', 'r') as input_file:
    data = [line.strip() for line in input_file.readlines()]
    # Make each line (which is a tab-separated string in a list) its own list of integers
    del(data[-1])
    for i in range(0, len(data)):
        data[i] = data[i].split('\t')
        data[i] = [int(n) for n in data[i]]


def difference_max_min(numbers):
    max = numbers[0]
    min = numbers[0]
    for number in numbers:
        if number > max:
            max = number
        elif number < min:
            min = number
    return max - min


def only_integer_quotient(numbers):
    for i in numbers:
        for j in numbers:
            if i != j and i % j == 0:
                return i // j


difference_max_min_checksum = 0
only_integer_quotient_checksum = 0

for row in data:
    difference_max_min_checksum += difference_max_min(row)
    only_integer_quotient_checksum += only_integer_quotient(row)

print(difference_max_min_checksum)
print(only_integer_quotient_checksum)

