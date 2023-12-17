#! /usr/bin/python

import sys, re

def count_arrangements(space, gaps):
    if gaps == 0:
        return 1

    counts = [1] * (space + 1)
    for _ in range(gaps - 1):
        counts = [ sum(counts[:j]) for j in range(1, len(counts) + 1) ]
    return sum(counts)

def count_matches(pattern, numbers):
    if not numbers:
        return 0 if "#" in pattern else 1

    min_size = sum(numbers) + len(numbers) - 1
    pattern = pattern.lstrip('.')

    if len(pattern) < min_size:
        return 0

    if pattern[0] == '#':
        if any(c == '.' for c in pattern[:numbers[0]]):
            return 0
        if len(pattern) > numbers[0] and pattern[numbers[0]] == '#':
            return 0
        return count_matches(pattern[numbers[0]+1:], numbers[1:])

    rest = pattern.lstrip("?")
    num_unknown = len(pattern) - len(rest)

    if not rest:
        space = num_unknown - min_size
        gaps = len(numbers)
        return count_arrangements(space, gaps)

    matches = 0

    for n in range(len(numbers) + 1):
        space = num_unknown - sum(numbers[:n]) - n
        if rest[0] == '.':
            space += 1
        if space < 0:
            break
        gaps = n
        matches += count_arrangements(space, gaps) * \
                   count_matches(rest, numbers[n:])

        if rest[0] == '#' and n < len(numbers):
            for j in range(1, numbers[n]):
                if space >= j:
                    matches += count_arrangements(space - j, gaps) * \
                               count_matches(rest, [numbers[n] - j] + numbers[n+1:])

    return matches

filename = sys.argv[1] if len(sys.argv) > 1 else "input.txt"

total = 0
expand = 5
with open(filename) as f:
    for row, line in enumerate(f):
        pattern, numbers = line.split(" ")
        pattern = "?".join([pattern] * expand)
        numbers = [ int(num) for num in numbers.split(",") ] * expand
        combinations = count_matches(pattern, numbers)
        print(row, pattern, numbers, combinations)
        total += combinations
print(total)
