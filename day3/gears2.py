#! /usr/bin/python

import re, sys

filename = sys.argv[1] if len(sys.argv) > 1 else "input.txt"
lines = open(filename).readlines()

def get_partnos(lineno, col):
    partnos = []

    for line in lines[max(lineno - 1, 0) : min(lineno + 2, len(lines))]:
        for m in re.finditer('\d+', line):
            if col in range(m.span()[0] - 1, m.span()[1] + 1):
                partnos.append(int(m[0]))

    return partnos

total = 0

for lineno, line in enumerate(lines):
    for m in re.finditer('\*', line):
        col, lastcol = m.span()
        partnos = get_partnos(lineno, m.span()[0])
        print(lineno, col, partnos)
        if len(partnos) == 2:
            total += partnos[0] * partnos[1]

print(total)
