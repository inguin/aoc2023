#! /usr/bin/python

import sys, re

filename = sys.argv[1] if len(sys.argv) > 1 else "input.txt"
lines = [ line.strip() for line in open(filename).readlines() ]
height = len(lines)
width = len(lines[0])

distances = [ ([999] * width) for _ in range(height) ]
next_nodes = []

for row, line in enumerate(lines):
    if "S" in line:
        col = line.index("S")
        distances[row][col] = 0
        next_nodes.append((row, col, 0))

while next_nodes:
    row, col, distance = next_nodes.pop()
    for nrow, ncol in ((row-1, col), (row+1, col), (row, col-1), (row,col+1)):
        if (nrow in range(width) and ncol in range(height) and
                lines[nrow][ncol] == '.' and
                distances[nrow][ncol] > distance + 1):
            distances[nrow][ncol] = distance + 1
            next_nodes.append((nrow, ncol, distance + 1))

steps = 6 if width < 20 else 64
print(sum(dist <= steps and dist % 2 == 0 for dline in distances for dist in dline))
