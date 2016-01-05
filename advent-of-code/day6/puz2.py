# starsparrow
# adventofcode puzzle 6-2

import re

with open('input.txt', 'r') as f:
	while True:
		read_data = f.read().splitlines()
		if not read_data:
			break
		stringlist = read_data