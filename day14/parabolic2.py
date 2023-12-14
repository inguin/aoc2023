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
for i in range(100000):
    cache.append(lines)
    lines = roll_and_spin(lines)
    lines = roll_and_spin(lines)
    lines = roll_and_spin(lines)
    lines = roll_and_spin(lines)

    print()
    print(f"After {i} cylces, weight = {weight(lines)}")
    for line in lines:
        print(line)

    if lines in cache:
        idx = cache.index(lines)
        print(f"Pattern after {i} cycles same as after {idx} cycles")
        break
