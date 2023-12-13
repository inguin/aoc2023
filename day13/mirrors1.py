#! /usr/bin/python

import sys, re

def find_reflection(lines):
    for line in lines:
        print(line)

    possible_reflections = set()
    for row, line in enumerate(lines):
        for ref in list(possible_reflections):
            cmp_row = ref - 1 - (row - ref)
            if cmp_row < 0:
                return ref
            if line != lines[cmp_row]:
                possible_reflections.remove(ref)
        if row > 0 and line == lines[row - 1]:
            possible_reflections.add(row)
    return possible_reflections.pop() if possible_reflections else 0

def flip(lines):
    flipped = []
    for col in range(len(lines[0])):
        flipped.append("".join(line[col] for line in lines))
    return(flipped)

def evaluate(lines):
    if row := find_reflection(lines):
        print(f"Reflection in row {row}")
        return 100 * row
    if col := find_reflection(flip(lines)):
        print(f"Reflection in column {col}")
        return col
    print("No reflection")
    return 0

filename = sys.argv[1] if len(sys.argv) > 1 else "input.txt"

total = 0

with open(filename) as f:
    lines = []
    for line in f:
        line = line.strip()
        if not line:
            total += evaluate(lines)
            lines = []
        else:
            lines.append(line)

if lines:
    total += evaluate(lines)

print(total)
