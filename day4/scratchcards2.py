#! /usr/bin/python

import sys

filename = sys.argv[1] if len(sys.argv) > 1 else "input.txt"

scores = []

with open(filename) as f:
    for line in f:
        day, line = line.strip().split(": ", 1)
        winning, got = line.split(" | ", 1)
        count = len(set(winning.split()) & set(got.split()))
        scores.append(count)

copies = [1] * len(scores)

for i, score in enumerate(scores):
    for j in range(i + 1, i + score + 1):
        copies[j] += copies[i]

print(sum(copies))
