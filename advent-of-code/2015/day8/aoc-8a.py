#! /usr/bin/env python

# Advent of Code 2015 - Day 8: Matchsticks - Puzzle A
# starsparrow

import codecs, re

f = open('input', 'r')
strings = f.readlines()
f.close()

def translate(matchobj):
	return "x" #codecs.decode(matchobj.group(0), "hex")

def clean(string):
	cleaned = string.lstrip('"').rstrip('"\n')
	cleaned = cleaned.replace('\\"', '"').replace('\\\\', '\\')
	cleaned = re.sub(r'\\x..',
					 translate,
					 cleaned)
	return cleaned

code_charcount = 0
mem_charcount = 0

for string in strings:
	code_charcount += len(list(string.rstrip('\n')))
	mem_charcount += len(list(clean(string)))
	print(string)

print("Code character count: {}\n\
Memory character count: {}\n\
Difference: {}".format(
	code_charcount,
	mem_charcount,
	code_charcount - mem_charcount
	)
)
