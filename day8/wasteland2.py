#! /usr/bin/python

import math, re, sys

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

def count_steps(node):
    steps = 0
    next_dir = dir_generator()

    while not node.endswith("Z"):
        steps += 1
        node = nodes[node][next(next_dir)]

    return steps

start_nodes = [ key for key in nodes.keys() if key.endswith("A") ]
path_steps = [ count_steps(node) for node in start_nodes ]
print(math.lcm(*path_steps))
