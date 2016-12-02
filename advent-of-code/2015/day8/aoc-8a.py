#! /usr/bin/env python

# Advent of Code 2015 - Day 8: Matchsticks - Puzzle A
# starsparrow

f = open('input', 'r')
strings = f.readlines()
f.close()

for string in strings:
	escaped = string.lstrip('"').rstrip('"\n')	
	escaped = escaped.replace('\\"', '"')
	escaped = escaped.replace('\\\\', '\\')
	print(escaped)

