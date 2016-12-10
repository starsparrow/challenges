#! /usr/bin/env python

# Advent of Code 2016 - Day 5: How About a Nice Game of Chess? - Puzzle A
# starsparrow

import hashlib, time

input = 'ugkcyxxp'

password = []

start_time = time.time()

hashindex = 0
while len(password) < 8:
	code = "{}{}".format(input, hashindex)
	hashinput = bytes(code, 'utf-8')
	md5hash = hashlib.md5(hashinput).hexdigest()
	if md5hash[0:5] == '00000':
		password.append(md5hash[5:6])
	hashindex += 1

print("".join(password))
print("--- Found answer in {} seconds ---".format(time.time() - start_time))