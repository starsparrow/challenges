#! /usr/bin/env python

# Advent of Code 2016 - Day 8: Two-Factor Authentication - Puzzle A
# starsparrow


# Class definition

class Display:
	"""Pixels! Woohoo!"""
	
	def __init__(self, resolution):
		self.pixels = {}
		self.resolution = resolution
		for x in range(0, resolution[0]):
			for y in range(0, resolution[1]):
				self.pixels[(x, y)] = '.'

	def rect(self, w, h):
		"""Turns on all of the pixels at the top-left of the screen which is
		w wide and h tall.
		"""
		pixels_to_turn_on = []
		for pixel in self.pixels:
			if pixel[0] < w and pixel[1] < h:
				pixels_to_turn_on.append(pixel)
		for pixel in pixels_to_turn_on:
			self.pixels[pixel] = '#'

	def rotate_row(self, row):
		"""Shift pixels in row right 1 pixel"""
		active_pixels = sorted([pixel for pixel in self.pixels if pixel[1] == row and
			self.pixels[pixel] == '#'])
		updated_pixels = []
		for pixel in active_pixels:
			if pixel[0] < self.resolution[0] - 1:
				new_y = pixel[0] + 1
			else:
				new_y = (pixel[0] + 1) % self.resolution[0]
			updated_pixels.append((new_y, pixel[1]))
		for pixel in active_pixels:
			self.pixels[pixel] = '.'
		for pixel in updated_pixels:
			self.pixels[pixel] = '#'

	def rotate_column(self, col):
		"""Shift pixels in column down 1 pixel"""
		active_pixels = sorted([pixel for pixel in self.pixels if pixel[0] == col and
			self.pixels[pixel] == '#'])
		updated_pixels = []
		for pixel in active_pixels:
			if pixel[1] < self.resolution[1] - 1:
				new_x = pixel[1] + 1
			else:
				new_x = (pixel[1] + 1) % self.resolution[1]
			updated_pixels.append((pixel[0], new_x))
		for pixel in active_pixels:
			self.pixels[pixel] = '.'
		for pixel in updated_pixels:
			self.pixels[pixel] = '#'

	def show(self):
		"""Show the display."""
		return '\n'.join(''.join([self.pixels[(x,y)] for x in range(0, self.resolution[0])])
			for y in range(0, self.resolution[1]))


# Main section

f = open('input', 'r')
instructions = [line.strip() for line in f.readlines()]
f.close()

screen = Display((50,6))
screen.rect(4,2)
for n in range(11):
	screen.rotate_column(0)
for n in range(5):
	screen.rotate_row(5)
print('\n')
print(screen.show())