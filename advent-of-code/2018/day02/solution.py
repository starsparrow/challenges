#!/usr/bin/python

from sys import argv

with open(argv[1], 'r') as input_file:
    data = [line.rstrip() for line in input_file.readlines()]


def contains_n(frequency, n):
    for letter in frequency:
        if frequency[letter] == n:
            return True
    return False


def get_frequency(line):
    letter_frequency = {}
    for letter in line:
        if letter not in letter_frequency:
            letter_frequency[letter] = 1
        else:
            letter_frequency[letter] += 1
    return letter_frequency


contains_two = 0
contains_three = 0

for line in data:
    frequency = get_frequency(line)
    if contains_n(frequency, 2):
        contains_two += 1
    if contains_n(frequency, 3):
        contains_three += 1
    
print(contains_two * contains_three)

for i in range(0, len(data) - 2):
    for j in range(i, len(data) - 1):
        difference_count = 0
        comparison = zip(list(data[i]), list(data[j])) 
        for pair in comparison:
            if pair[0] != pair[1]:
                difference_count += 1
        if difference_count == 1:
            print(data[i], data[j])
