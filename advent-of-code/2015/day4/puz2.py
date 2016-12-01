# starsparrow
# adventofcode puzzle 4-2

import hashlib

i = 1
key = 'yzbqklnj'

match = False

while not match:
	input = key + str(i)
	m = hashlib.md5(input.encode('utf-8')).hexdigest()
	if m[0:6] == '000000':
		match = True
	else:
		i += 1
		
print(i)