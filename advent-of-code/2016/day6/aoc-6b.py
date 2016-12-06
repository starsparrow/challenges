#! /usr/bin/env python

# Advent of Code 2016 - Day 6: Signals and Noise - Puzzle B
# starsparrow

f = open('input', 'r')
signal = [line.strip() for line in f.readlines()]
f.close

def most_common(list):
	'''Return the most common letter in a list of letters'''

	frequency = {}
	for letter in list:
		if letter in frequency.keys():
			frequency[letter] += 1
		else:
			frequency[letter] = 1
	# Literally all that is different between today's puzzles is the reverse...
	max_freq = sorted(frequency.values(), reverse=False)[0]
	for letter in list:
		if frequency[letter] == max_freq:
			return letter

def enhance(signal):
	'''Split each line into columns, find most common letter in each column
	and join them together to get the error-corrected message'''

	msg_length = len(signal[0])

	columns = {}
	for n in range(0, msg_length):
		columns[n] = []

	for message in signal:
		letters = list(message)
		for n in range(0, msg_length):
			columns[n].append(letters[n])

	error_corrected = []
	for position in columns:
		error_corrected.append(most_common(columns[position]))
	print("".join(error_corrected))
		
enhance(signal)
