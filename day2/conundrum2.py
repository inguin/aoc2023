#! /usr/bin/python

import re, sys

filename = sys.argv[1] if len(sys.argv) > 1 else "input.txt"
total = 0

with open(filename) as f:
    for line in f:
        m = re.match("Game (\d+): (.*)", line)
        game_id, line = int(m[1]), m[2]

        maxima = { "red": 0, "green": 0, "blue": 0 }

        for subset in line.split("; "):
            for cube in subset.split(", "):
                count, color = cube.split(" ", 1)
                maxima[color] = max(maxima[color], int(count))

        power = maxima["red"] * maxima["green"] * maxima["blue"]
        print(f"Game {game_id}: {power}")
        total += power

print(total)
