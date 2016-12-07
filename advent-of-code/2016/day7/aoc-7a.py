#! /usr/bin/env python

# Advent of Code 2016 - Day 7: Signals and Noise - Puzzle A
# starsparrow

f = open('input', 'r')
input = [line.strip() for line in f.readlines()]
f.close()


# Function definitions

def detect_abba(addr_part):
	"""Checks for ABBA sequence in supplied string. Returns True/False."""
	charlist = list(addr_part)
	while len(charlist) > 3:
		if (charlist[0] == charlist[3] and
			charlist[1] == charlist[2] and
			charlist[0] != charlist[1]):
			return True
		else:
			charlist.remove(charlist[0])
	
	return False # Only do this if a match not found in the above loop


def parse_address(addr):
	"""Get normal and hypernet sequences and return them in a dict."""
	charlist = list(addr)
	norm_seq = []
	hyper_seq_builder = []
	hyper_seqs = []
	
	while len(charlist) > 0:
		if charlist[0] == ']': # Process the hypersequence list when completed
			charlist.remove(charlist[0])
			hyper_seqs.append("".join(hyper_seq_builder))
			hyper_seq_builder = []
		elif charlist[0] != '[': # Normal sequence
			norm_seq.append(charlist[0])
			charlist.remove(charlist[0])
		else: # Hypernet sequence encountered!
			charlist.remove(charlist[0]) # Discard the [ character
			while charlist[0] != ']':
				hyper_seq_builder.append(charlist[0])
				charlist.remove(charlist[0])

	return {'norm_seq': "".join(norm_seq), 'hyper_seqs': hyper_seqs}


def supports_tls(addr):
	address_parts = parse_address(addr)
	for seq in address_parts['hyper_seqs']:
		if detect_abba(seq):
			return False
	if detect_abba(address_parts['norm_seq']):
		return True


def main():
	tls_addresses = []
	for address in input:
		if supports_tls(address):
			tls_addresses.append(address)
			print("{}\t{}".format(address, supports_tls(address)))
	print(len(tls_addresses))


# Main section

main()
