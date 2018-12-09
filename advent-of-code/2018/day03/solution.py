#!/usr/bin/env python

from sys import argv


def get_claim_id(claim):
    return claim[0].lstrip('#')


def get_square_inches_in_claim(claim):

    origin = claim[2].rstrip(':').partition(',')
    origin = (int(origin[0]), int(origin[2]))
    dimensions = claim[3].partition('x')
    dimensions = (int(dimensions[0]), int(dimensions[2]))
    
    square_inches = []
    for x in range(0, dimensions[0]):
        for y in range(0, dimensions[1]):
            square_inches.append((origin[0] + x, origin[1] + y))

    return square_inches


with open(argv[1], 'r') as input_file:
    claim_list = [line.rstrip().split() for line in input_file.readlines()]


# Puzzle 1

claimed_square_inches = {}

for claim in claim_list:
    for square_inch in get_square_inches_in_claim(claim):
        if square_inch not in claimed_square_inches:
            claimed_square_inches[square_inch] = []
        claimed_square_inches[square_inch].append(get_claim_id(claim))

overlapping_claimed_square_inches = 0

for square_inch in claimed_square_inches:
    claims = claimed_square_inches[square_inch]
    if len(claims) > 1:
        overlapping_claimed_square_inches += 1

print("Number of overlapping claimed square inches: {}".format(
    overlapping_claimed_square_inches))


# Puzzle 2

for claim in claim_list:
    claim_id = get_claim_id(claim)
    square_inches = get_square_inches_in_claim(claim)
    unique_claim_flag = True
    for square_inch in square_inches:
        if len(claimed_square_inches[square_inch]) > 1:
            unique_claim_flag = False
    if unique_claim_flag:
        print("Claim with ID #{} is a unique claim!".format(claim_id))

