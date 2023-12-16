#! /usr/bin/python

import sys, re

filename = sys.argv[1] if len(sys.argv) > 1 else "input.txt"
lines = [ line.strip() for line in open(filename).readlines() ]

height = len(lines)
width = len(lines[0])
energized = [ [ False ] * width for _ in range(height) ]

NORTH = (-1, 0)
EAST = (0, 1)
SOUTH = (1, 0)
WEST = (0, -1)

followed = set()

def follow_beam(row, col, direction):
    if (row, col, direction) in followed:
        return
    followed.add((row, col, direction))

    while row in range(height) and col in range(width):
        energized[row][col] = True
        tile = lines[row][col]

        if direction in (NORTH, SOUTH) and tile == '-':
            follow_beam(row, col - 1, WEST)
            follow_beam(row, col + 1, EAST)
            return
        elif direction in (EAST, WEST) and tile == '|':
            follow_beam(row - 1, col, NORTH)
            follow_beam(row + 1, col, SOUTH)
            return
        elif direction == NORTH:
            if tile == '/': direction = EAST
            elif tile == '\\': direction = WEST
        elif direction == EAST:
            if tile == '/': direction = NORTH
            elif tile == '\\': direction = SOUTH
        elif direction == SOUTH:
            if tile == '/': direction = WEST
            elif tile == '\\': direction = EAST
        elif direction == WEST:
            if tile == '/': direction = SOUTH
            elif tile == '\\': direction = NORTH

        row += direction[0]
        col += direction[1]

follow_beam(0, 0, EAST)

for line in energized:
    print("".join('#' if v else '.' for v in line))

print(sum(v for line in energized for v in line))
