#! /usr/bin/python

import sys, re

filename = sys.argv[1] if len(sys.argv) > 1 else "input.txt"

headings = ['R', 'D', 'L', 'U']

row = 0
col = 0
hlines = []
vlines = []

def count_row_pixels(row):
    crossed_vlines = sorted((vl[0], vl[1] > vl[2]) for vl in vlines
                            if row >= min(vl[1], vl[2]) and row <= max(vl[1], vl[2]))
    crossed_hlines = sorted((hl[0], hl[1]) for hl in hlines if hl[2] == row)

    pixels = 0
    last_col = 0
    last_up = False
    inside = False
    last_draw = False

    for col, up in crossed_vlines:
        draw = any(col == hl[1] for hl in crossed_hlines) or inside

        if draw:
            pixels += (col - last_col)
        elif last_draw:
            pixels += 1

        if up != last_up:
            inside = not inside

        last_col = col
        last_up = up
        last_draw = draw

    if last_draw:
        pixels += 1
    return pixels

with open(filename) as f:
    for line in f:
        digits = re.match(". \d+ \(#(.+)\)", line)[1]
        dist = int(digits[:5], 16)
        heading = headings[int(digits[5])]

        if heading == 'U':
            vlines.append((col, row, row - dist))
            row -= dist
        elif heading == 'D':
            vlines.append((col, row, row + dist))
            row += dist
        elif heading == 'R':
            hlines.append((col, col + dist, row))
            col += dist
        elif heading == 'L':
            hlines.append((col - dist, col, row))
            col -= dist

breakrows = set()
for vline in vlines:
    breakrows.add(vline[1])
    breakrows.add(vline[2])

last_breakrow = None
total = 0

for row in sorted(breakrows):
    total += count_row_pixels(row)
    if last_breakrow is not None:
        total += (row - last_breakrow - 1) * count_row_pixels(row - 1)
    last_breakrow = row

print(total)
