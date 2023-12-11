#! /usr/bin/python

import sys, re

filename = sys.argv[1] if len(sys.argv) > 1 else "input.txt"

galaxies = []

with open(filename) as f:
    for row, line in enumerate(f):
        for m in re.finditer('#', line):
            galaxies.append([row, m.span()[0]])

print("before expansion:", galaxies)

expand_rows = [ row for row in range(max(pos[0] for pos in galaxies))
                if not any(galaxy[0] == row for galaxy in galaxies) ]

expand_cols = [ col for col in range(max(pos[1] for pos in galaxies))
                if not any(galaxy[1] == col for galaxy in galaxies) ]

for galaxy in galaxies:
    galaxy[0] += sum(galaxy[0] > row for row in expand_rows)
    galaxy[1] += sum(galaxy[1] > col for col in expand_cols)

print("after expansion:", galaxies)

total = 0
for i in range(len(galaxies)):
    for j in range(i + 1, len(galaxies)):
        dist = abs(galaxies[i][0] - galaxies[j][0]) + abs(galaxies[i][1] - galaxies[j][1])
        print(f"Galaxies {i} and {j}: {dist}")
        total += dist
print(total)
