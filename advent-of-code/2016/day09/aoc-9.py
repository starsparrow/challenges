#! /usr/bin/env python

# Advent of Code 2016 - Day 9: Explosives in Cyberspace
# starsparrow


with open('input.txt', 'r') as f:
    data = f.readlines()[0].rstrip()


def decompressv1(data):
    compressed = list(data)
    decompressed = []
    while len(compressed) > 0:
        if compressed[0] != '(':
            decompressed.append(compressed[0])
            del compressed[0]
        else:
            marker_end = compressed.index(')')
            marker = ''.join([compressed[n] for n in range(marker_end + 1)])
            for n in range(len(marker)):
                del compressed[0]
            marker = marker.lstrip('(').rstrip(')').partition('x')
            chars, copies = int(marker[0]), int(marker[2])
            string_to_copy = ''.join([compressed[n] for n in range(chars)])
            for n in range(chars):
                del compressed[0]
            for i in range(copies):
                decompressed.append(string_to_copy)
    return ''.join(decompressed)


def decompressv2(data):
    compressed = list(data)
    decompressed = []
    while len(compressed) > 0:
        if compressed[0] != '(':
            decompressed.append(compressed[0])
            del compressed[0]
        else:
            marker_end = compressed.index(')')
            marker = ''.join([compressed[n] for n in range(marker_end + 1)])
            for n in range(len(marker)):
                decompressed.append(compressed[0])
            marker = marker.lstrip('(').rstrip(')').partition('x')
            chars, copies = int(marker[0]), int(marker[2])
            string_to_copy = ''.join([compressed[n] for n in range(chars)])
            for n in range(chars):
                del compressed[0]
            for i in range(copies):
                decompressed.append(string_to_copy)
    return ''.join(decompressed)


print(len(decompressv1(data)))  # Puzzle A

