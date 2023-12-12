#! /usr/bin/python

import sys, re

def trim_line(pattern, numbers):
    first_unknown = pattern.find("?")
    if first_unknown == -1:
        return "", []

    before = pattern[:first_unknown]
    pattern = pattern[first_unknown:]

    for group in re.findall("#+", before):
        if numbers[0] == len(group):
            numbers = numbers[1:]
        else:
            numbers[0] -= len(group)

    last_unknown = pattern.rfind("?")
    after = pattern[last_unknown+1:]
    pattern = pattern[:last_unknown+1]

    for group in reversed(re.findall("#+", after)):
        if numbers[-1] == len(group):
            numbers = numbers[:-1]
        else:
            numbers[-1] -= len(group)

    return pattern, numbers

def generate_patterns(length, numbers):
    if len(numbers) == 1:
        max_space = length - numbers[0]
        for space in range(max_space + 1):
            yield "." * space + "#" * numbers[0] + "." * (max_space - space)
        return

    max_space = length - sum(numbers) - len(numbers) + 1
    for space in range(max_space + 1):
        pattern = "." * space + "#" * numbers[0]
        for rest in generate_patterns(length - len(pattern) - 1, numbers[1:]):
            yield pattern + "." + rest

def pattern_matches(pattern, given):
    return all(c1 == c2 or c2 == "?" for c1, c2 in zip(pattern, given))

def find_combinations(pattern, numbers):
    #pattern, numbers = trim_line(pattern, numbers)
    if not pattern:
        return 1

    combinations = 0

    for result in generate_patterns(len(pattern), numbers):
        if pattern_matches(result, pattern):
            combinations += 1

    return combinations

filename = sys.argv[1] if len(sys.argv) > 1 else "input.txt"

total = 0
with open(filename) as f:
    for line in f:
        pattern, numbers = line.split(" ")
        numbers = [ int(num) for num in numbers.split(",") ]
        combinations = find_combinations(pattern, numbers)
        print(pattern, numbers, combinations)
        total += combinations
print(total)
