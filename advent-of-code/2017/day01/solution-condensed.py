from sys import argv

numbers = [int(n) for n in argv[1].strip()]

def matching_sum(interval):
    running_total = 0
    for i in range(0, len(numbers)):
        j = i + interval if i < len(numbers) - interval else i + interval - len(numbers)
        if numbers[i] == numbers[j]:
            running_total += numbers[i]
    return running_total

print(matching_sum(1))
print(matching_sum(len(numbers) // 2))
