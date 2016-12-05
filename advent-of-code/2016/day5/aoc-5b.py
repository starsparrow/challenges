#! /usr/bin/env python

# Advent of Code 2016 - Day 5: How About a Nice Game of Chess? - Puzzle B
# starsparrow

import hashlib

input = 'abc'

password = {
	0: "",
	1: "",
	2: "",
	3: "",
	4: "",
	5: "",
	6: "",
	7: ""
}

hashindex = 0
while hashindex < 5000000:
	code = "{0}{1}".format(input, hashindex)
	hashinput = bytes(code, 'utf-8')
	md5hash = hashlib.md5(hashinput).hexdigest()
	if (md5hash[0:5] == '00000'):
		if (md5hash[5:6] in [0,1,2,3,4,5,6,7] and 
			password[md5hash[5:6]] == ""):
				password[md5hash[5:6]] = md5hash[6:7]
	hashindex += 1

print(password)
