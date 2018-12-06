#!/usr/bin/python

from sys import argv

with open(argv[1], 'r') as input_file:
    data = [line.rstrip() for line in input_file.readlines()]


current_frequency = 0
final_frequency = None
frequency_history = [0]
frequency_processed = False
first_repeat = None

while first_repeat == None:
    for line in data:
        operator = line[0]
        value = int(line[1:])
    
        if operator == '+':
            current_frequency += value
        elif operator == '-':
            current_frequency -= value

        if first_repeat == None and current_frequency in frequency_history:
            first_repeat = current_frequency

        frequency_history.append(current_frequency)

    if frequency_processed == False:
        frequency_processed = True
        final_frequency = current_frequency

print("The final frequency is {}.".format(final_frequency))
print("The first repeated frequency is {}.".format(first_repeat))

