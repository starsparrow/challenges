#!/usr/bin/env python3

from sys import argv


with open(argv[1], 'r') as input_file:
    memory_banks = [int(n) for n in input_file.readlines()[0].strip().split(' ' * 3)]


def get_max_block_value(memory_banks):
    max_block_value = 0
    for block in memory_banks:
        max_block_value = block if block > max_block_value else max_block_value
    return max_block_value


def get_first_max_block_value_index(memory_banks):
    return memory_banks.index(get_max_block_value(memory_banks))


def redistribute_blocks(memory_banks):
    start_index = get_first_max_block_value_index(memory_banks)
    number_of_blocks = get_max_block_value(memory_banks)
    memory_banks[start_index] = 0
    for i in range(1, number_of_blocks + 1):
       index = start_index + i if start_index + i < len(memory_banks) else (start_index + i) % len(memory_banks)
       memory_banks[index] += 1
    return memory_banks


def main():
    global memory_banks
    history = []
    while memory_banks not in history:
        history.append(memory_banks[:])
        memory_banks = redistribute_blocks(memory_banks)
    print(len(history))


if __name__ == "__main__":
    main()

