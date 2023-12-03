#! /usr/bin/python

import re, sys

filename = sys.argv[1] if len(sys.argv) > 1 else "input.txt"
lines = open(filename).readlines()

def is_symbol(c):
    return c != '.' and c != '\n' and not c.isdigit()

def find_symbol(lineno, col, lastcol):
    for line in lines[max(lineno - 1, 0) : min(lineno + 2, len(lines))]:
        chars = line[max(col - 1, 0) : lastcol + 1]
        if any(is_symbol(c) for c in chars):
            return True
    return False

total = 0

for lineno, line in enumerate(lines):
    for m in re.finditer('\d+', line):
        col, lastcol = m.span()
        if find_symbol(lineno, col, lastcol):
            print(f"{m[0]} -> symbol")
            total += int(m[0])
        else:
            print(f"{m[0]} -> no symbol")

print(total)
