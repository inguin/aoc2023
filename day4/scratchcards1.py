#! /usr/bin/python

import sys

filename = sys.argv[1] if len(sys.argv) > 1 else "input.txt"

total = 0

with open(filename) as f:
    for line in f:
        day, line = line.strip().split(": ", 1)
        winning, got = line.split(" | ", 1)
        count = len(set(winning.split()) & set(got.split()))
        print(f"{day}: {count} matches")
        if count > 0:
            total += 2 ** (count - 1)

print(total)
