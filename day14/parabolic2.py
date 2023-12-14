#! /usr/bin/python

import sys, re

filename = sys.argv[1] if len(sys.argv) > 1 else "input.txt"
lines = [ line.strip() for line in open(filename).readlines() ]

def roll_and_spin(lines):
    new_lines = []
    for col in range(len(lines[0])):
        new_line = ""
        spaces = 0
        for line in lines:
            c = line[col]
            if c == 'O':
                new_line += 'O'
            elif c == '#':
                new_line += '.' * spaces + '#'
                spaces = 0
            else:
                spaces += 1
        new_lines.append((new_line + '.' * spaces)[::-1])
    return new_lines

def weight(lines):
    total = 0
    for row, line in enumerate(lines):
        for c in line:
            if c == 'O':
                total += len(lines) - row
    return total

cache = []

while not lines in cache:
    print()
    print(f"After {len(cache)} cycles, weight = {weight(lines)}:")
    for line in lines:
        print(line)

    cache.append(lines)

    lines = roll_and_spin(lines)
    lines = roll_and_spin(lines)
    lines = roll_and_spin(lines)
    lines = roll_and_spin(lines)

idx = cache.index(lines)

print()
print(f"Pattern after {len(cache)} cycles same as after {idx} cycles")

period = len(cache) - idx
max_cycles = 1000000000

for j in range(idx, len(cache)):
    if (j % period) == (max_cycles % period):
        print(f"Using weight from cycle {j}")
        print(f"Weight after {max_cycles} cycles:", weight(cache[j]))
