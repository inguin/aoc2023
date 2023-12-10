#! /usr/bin/python

import sys, re

filename = sys.argv[1] if len(sys.argv) > 1 else "input.txt"

lines = [ line.strip() for line in open(filename).readlines() ]

def find_neighbors(row, col):
    tile = lines[row][col]
    neighbors = []
    if tile in ("J", "L", "|", "S"):
        if lines[row - 1][col] in ("F", "7", "|"):
            neighbors.append("N")
    if tile in ("L", "F", "-", "S"):
        if lines[row][col + 1] in ("J", "7", "-"):
            neighbors.append("E")
    if tile in ("F", "7", "|", "S"):
        if lines[row + 1][col] in ("J", "L", "|"):
            neighbors.append("S")
    if tile in ("J", "7", "-", "S"):
        if lines[row][col - 1] in ("L", "F", "-"):
            neighbors.append("W")

    if len(neighbors) != 2:
        print(f"WTF? at line {row}, col {col}")
    return neighbors

def find_startpos():
    for row, line in enumerate(lines):
        if (col := line.find("S")) >= 0:
            print(f"Start: line {row}, col {col}")
            match find_neighbors(row, col):
                case ["N", "S"]: tile = '|'
                case ["E", "W"]: tile = '-'
                case ["N", "E"]: tile = 'L'
                case ["E", "S"]: tile = 'F'
                case ["S", "W"]: tile = '7'
                case ["N", "W"]: tile = 'J'
            print(f"Start tile: {tile}")
            lines[row] = lines[row].replace("S", tile)
            return row, col

def opposite(neighbor):
    match neighbor:
        case "N": return "S"
        case "E": return "W"
        case "S": return "N"
        case "W": return "E"

def advance(row, col, last_dir):
    for neighbor in find_neighbors(row, col):
        if neighbor == "N" and last_dir != "S":
            return (row - 1, col, neighbor)
        if neighbor == "E" and last_dir != "W":
            return (row, col + 1, neighbor)
        if neighbor == "S" and last_dir != "N":
            return (row + 1, col, neighbor)
        if neighbor == "W" and last_dir != "E":
            return (row, col - 1, neighbor)

in_loop = [ [False] * len(line) for line in lines ]
row1, col1 = row2, col2 = find_startpos()
dir1, dir2 = [ opposite(neigh) for neigh in find_neighbors(row1, col1) ]
steps = 0
in_loop[row1][col1] = True

while True:
    row1, col1, dir1 = advance(row1, col1, dir1)
    row2, col2, dir2 = advance(row2, col2, dir2)
    steps += 1

    in_loop[row1][col1] = True
    in_loop[row2][col2] = True

    if (row1, col1) == (row2, col2):
        break

total = 0

for row, line in enumerate(lines):
    inside = False
    for col, c in enumerate(line):
        if in_loop[row][col]:
            print('.', end="")
            if c == "|":
                inside = not inside
            elif c in ("L", "F"):
                start = c
            elif c == "7" and start == "L":
                inside = not inside
            elif c == "J" and start == "F":
                inside = not inside
        else:
            print("I" if inside else "O", end="")
            total += inside
    print()

print(total)
