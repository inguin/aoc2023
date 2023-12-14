#! /usr/bin/python

import sys, re

filename = sys.argv[1] if len(sys.argv) > 1 else "input.txt"
lines = [ line.strip() for line in open(filename).readlines() ]

total = 0

for col in range(len(lines[0])):
    pos_weight = len(lines)
    col_weight = 0
    for row, line in enumerate(lines):
        c = line[col]
        if c == 'O':
            col_weight += pos_weight
            pos_weight -= 1
        elif c == '#':
            pos_weight = len(lines) - row - 1
    print(f"Column {col}: weight {col_weight}")
    total += col_weight

print(total)
