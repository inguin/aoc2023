#! /usr/bin/python

import sys, re

filename = sys.argv[1] if len(sys.argv) > 1 else "input.txt"

row = 0
col = 0
trenches = []
last_tile = None

with open(filename) as f:
    last_heading = ''
    for line in f:
        heading, dist, color = re.match("(.) (\d+) \(#(.+)\)", line).groups()
        for _ in range(int(dist)):
            if heading == 'U': row -= 1
            elif heading == 'D': row += 1
            elif heading == 'R': col += 1
            elif heading == 'L': col -= 1

            tile = [row, col, heading == 'D']
            if last_tile and heading == 'U':
                last_tile[2] = True

            last_tile = tile

            trenches.append(tile)

min_row = min(t[0] for t in trenches)
max_row = max(t[0] for t in trenches)
height = max_row - min_row + 1

min_col = min(t[1] for t in trenches)
max_col = max(t[1] for t in trenches)
width = max_col - min_col + 1

grid = [ ['.'] * width for _ in range(height) ]
for row, col, has_down in trenches:
    grid[row - min_row][col - min_col] = '|' if has_down else '#'

total = 0

for line in grid:
    inside = False
    for c in line:
        if c == '|':
            inside = not inside
        total += (c != '.' or inside)
        print('#' if c != '.' or inside else '.', end="")
    print()

print(total)
