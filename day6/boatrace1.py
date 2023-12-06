#! /usr/bin/python

import sys, re

filename = sys.argv[1] if len(sys.argv) > 1 else "input.txt"
with open(filename) as f:
    line = f.readline()
    times = [ int(token) for token in re.findall("\d+", line) ]
    line = f.readline()
    distances = [ int(token) for token in re.findall("\d+", line) ]

combinations = 1

for time, distance in zip(times, distances):
    winning = sum(i * (time - i) > distance for i in range(time))
    print(winning)
    combinations *= winning

print(combinations)
