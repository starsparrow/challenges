#! /usr/bin/env python

# Advent of Code 2016 - Day 5: How About a Nice Game of Chess? - Puzzle B
# starsparrow

import hashlib, time

input = 'ugkcyxxp'

password = {0: "", 1: "", 2: "", 3: "", 4: "", 5: "", 6: "", 7: ""}

start_time = time.time()

hashindex = 0
while "" in password.values():
	code = "{0}{1}".format(input, hashindex)
	hashinput = bytes(code, 'utf-8')
	md5hash = hashlib.md5(hashinput).hexdigest()
	if (md5hash[0:5] == '00000'):
		if (md5hash[5:6] in [str(x) for x in range(0,8)] and 
			password[int(md5hash[5:6])] == ""):
				password[int(md5hash[5:6])] = md5hash[6:7]
	hashindex += 1

print("".join([password[place] for place in password]))
print("--- Found answer in {} seconds ---".format(time.time() - start_time))