#!/usr/bin/env python

from sys import argv

with open(argv[1], 'r') as input_file:
    passphrases = [line.strip() for line in input_file.readlines()]

low_security_valid_passphrases = []
high_security_valid_passphrases = []

for passphrase in passphrases:
    valid_passphrase = 1
    words = passphrase.split(' ')

    # Check for duplicate words
    while len(words) > 1:
        current_word = words.pop()
        if current_word in words:
            valid_passphrase = 0
    if valid_passphrase == 1:
        low_security_valid_passphrases.append(passphrase)

for passphrase in passphrases:
    valid_passphrase = 1
    words = [sorted(word) for word in passphrase.split(' ')]

    # Check for anagrams
    while len(words) > 1:
        current_word = words.pop()
        if current_word in words:
            valid_passphrase = 0
    if valid_passphrase == 1:
        high_security_valid_passphrases.append(passphrase)

print(len(low_security_valid_passphrases))
print(len(high_security_valid_passphrases))

