#! /usr/bin/python

import sys, re

filename = sys.argv[1] if len(sys.argv) > 1 else "input.txt"

nodes = {}

with open(filename) as f:
    directions = f.readline().strip()
    for line in f:
        if m := re.match("(.*) = \((.*), (.*)\)", line):
            nodes[m[1]] = (m[2], m[3])

def dir_generator():
    while True:
        for c in directions:
            yield 0 if c == 'L' else 1

steps = 0
node = "AAA"
next_dir = dir_generator()

while node != "ZZZ":
    steps += 1
    node = nodes[node][next(next_dir)]
    print(steps, node)
