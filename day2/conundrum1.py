#! /usr/bin/python

import re, sys

filename = sys.argv[1] if len(sys.argv) > 1 else "input.txt"
total = 0

with open(filename) as f:
    for line in f:
        m = re.match("Game (\d+): (.*)", line)
        game_id, line = int(m[1]), m[2]

        possible = True

        for subset in line.split("; "):
            for cube in subset.split(", "):
                count, color = cube.split(" ", 1)
                if (color == "red" and int(count) > 12) or \
                   (color == "green" and int(count) > 13) or \
                   (color == "blue" and int(count) > 14):
                    possible = False

        print(f"Game {game_id}: {possible}")
        if possible:
            total += game_id

print(total)
