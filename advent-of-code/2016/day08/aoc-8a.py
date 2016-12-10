#! /usr/bin/env python

# Advent of Code 2016 - Day 8: Two-Factor Authentication - Puzzle A
# starsparrow

f = open('input', 'r')
instructions = [line.strip() for line in f.readlines()]
f.close()


class Display:
	"""Pixels! Woohoo!"""
	
	def __init__(self):
		self.pixels = {}
		resolution = 50, 6 # width, height
		for x in range(0, resolution[0]):
			for y in range(0, resolution[1]):
				self.pixels[(x, y)] = 0

	def update(self, instruction):
		"""UPDATE"""
		inst_details = parse_instruction(instruction)
		action = inst_details[0]

	def rect(self, a, b):
		"""Turns on all of the pixels at the top-left of the screen which is
		A wide and B tall.
		"""
		pass

	def rotate_row(self, row, n):
		"""Shift row row right n pixels"""
		pass

	def rotate_column(self, col, n):
		"""Shift column col down n pixels"""
		pass

	def show(self):
		"""Show the display."""
		print(len(self.pixels.values()))


def main():
	"""UPDATE"""
	screen = Display()
	for instruction in instructions:
		screen.update(instruction)
	screen.show()


screen = Display()
screen.show()