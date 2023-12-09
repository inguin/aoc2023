#! /usr/bin/python

import sys, re

def extrapolate(seq):
    diffs = [ b - a for a, b in zip(seq[:-1], seq[1:]) ]
    if all(diff == 0 for diff in diffs):
        return seq[0]
    return seq[0] - extrapolate(diffs)

filename = sys.argv[1] if len(sys.argv) > 1 else "input.txt"
total = 0

with open(filename) as f:
    for line in f:
        seq = [ int(m) for m in line.split() ]
        val = extrapolate(seq)
        print(val)
        total += val

print(total)
