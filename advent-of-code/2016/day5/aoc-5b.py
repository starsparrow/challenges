#! /usr/bin/env python

# Advent of Code 2016 - Day 5: How About a Nice Game of Chess? - Puzzle B
# starsparrow

import hashlib

input = 'ugkcyxxp'

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
while "" in password.values():
	code = "{}{}".format(input, hashindex)
	hashinput = bytes(code, 'utf-8')
	md5hash = hashlib.md5(hashinput).hexdigest()
	if (md5hash[0:5] == '00000' and
		md5hash[5:6] in range(0,8) and 
		password[md5hash[5:6]] != ""):
			password[md5hash[5:6]] = md5hash[6:7]
			print(password)
	hashindex += 1
