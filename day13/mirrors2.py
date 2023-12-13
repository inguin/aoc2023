#! /usr/bin/python

import sys, re

def count_smudges(line1, line2):
    return sum(a != b for a, b in zip(line1, line2))

def find_reflection(lines):
    for line in lines:
        print(line)

    possible_reflections = {} # value is number of smudges
    for row, line in enumerate(lines):
        for ref, smudges in list(possible_reflections.items()):
            cmp_row = ref - 1 - (row - ref)
            if cmp_row < 0 and smudges == 1:
                return ref
            smudges += count_smudges(line, lines[cmp_row])
            if smudges > 1:
                del(possible_reflections[ref])
            else:
                possible_reflections[ref] = smudges
        if row > 0:
            if (smudges := count_smudges(line, lines[row - 1])) < 2:
                possible_reflections[row] = smudges

    for row, smudges in possible_reflections.items():
        if smudges == 1:
            return row
    return 0

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
