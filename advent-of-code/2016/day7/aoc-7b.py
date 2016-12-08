#! /usr/bin/env python

# Advent of Code 2016 - Day 7: Internet Protocol Version 7 - Puzzle B
# starsparrow

import re

f = open('input', 'r')
input = [line.strip() for line in f.readlines()]
f.close()


# Function definitions

def detect_abba(addr_part):
    """Checks for ABBA sequence in supplied string. Returns the ABBA."""
    charlist = list(addr_part)
    while len(charlist) > 3:
        if (charlist[0] == charlist[3] and
			charlist[1] == charlist[2] and
			charlist[0] != charlist[1]):
                return "".join(charlist[0:4])
        else:
            charlist.remove(charlist[0])
    return False # Only do this if a match not found in the above loop


def detect_aba(addr_part):
    """Checks for ABA sequence in supplied string. Returns the ABA."""
    charlist = list(addr_part)
    while len(charlist) > 2:
        if (charlist[0] == charlist[2] and
            charlist[0] != charlist[1]):
         return "".join(charlist[0:3])
        else:
            charlist.remove(charlist[0])
    return False # Only do this if a match not found in the above loop
    
    
def detect_bab(aba, addr_part):
    """For a provided ABA, check whether a corresponding BAB exists in the
    provided string. Returns True/False.
    """
    charlist = list(aba)
    bab = "".join([charlist[1], charlist[0], charlist[1]])
    return bab in addr_part


def parse_address(addr):
	"""Get normal and hypernet sequences and return them in a dict."""
	address = addr
	norm_seqs = []
	hyper_seqs = []

	while len(list(address)) > 0:
		if list(address)[0] != '[':
			m = re.search('^[a-z]+', address)
			norm_seqs.append(m.group(0))
		else:
			m = re.search('\[[a-z]+\]', address)
			hyper_seqs.append(m.group(0))
		
		address = list(address)
		for n in range(0, len(m.group(0))):
			address.remove(address[0])
		address = "".join(address)

	return {'norm_seqs': norm_seqs, 'hyper_seqs': hyper_seqs}


def supports_tls(addr):
	"""Make sure the hypernets don't have any ABBAs, and at least one ABBA can
	be found in the normal address sequences. Return True if so.
	"""
	address_parts = parse_address(addr)
	for seq in address_parts['hyper_seqs']:
		if detect_abba(seq):
			return False
	for seq in address_parts['norm_seqs']:
		if detect_abba(seq):
			return True
			

def supports_ssl(addr):
    """Make sure the supernets have at least one ABA and that there is a
    corresponding BAB in at least one of the hypernets.
    """
    address_parts = parse_address(addr)
    for normseq in address_parts['norm_seqs']:
        if detect_aba(normseq):
            for hyperseq in address_parts['hyper_seqs']:
                if detect_bab(detect_aba(normseq), hyperseq):
                    return True


def main():
	tls_addresses = []
	ssl_addresses = []
	for address in input:
		if supports_tls(address):
			tls_addresses.append(address)
		if supports_ssl(address):
		    ssl_addresses.append(address)
	print('{} addresses support TLS.'.format(len(tls_addresses)))
	print('{} addresses support SSL.'.format(len(ssl_addresses)))


# Main section

main()
