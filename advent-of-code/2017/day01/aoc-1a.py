#!/usr/bin/env python

from sys import argv


with open(argv[1], 'r') as input:
    numbers = [int(n) for n in input.read().strip()]


def matching_sum(interval):
    running_total = 0

    for i in range(0, len(numbers)):
        j = i + interval if i < len(numbers) - interval else i + interval - len(numbers)
        if numbers[i] == numbers[j]:
            running_total += numbers[i]

    return running_total


def consecutive_matching_sum():
    return matching_sum(1)


def opposite_matching_sum():
    return matching_sum(len(numbers) // 2)


print(consecutive_matching_sum())
print(opposite_matching_sum())

