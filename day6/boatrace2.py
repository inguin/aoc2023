#! /usr/bin/python

import sys, re

filename = sys.argv[1] if len(sys.argv) > 1 else "input.txt"
with open(filename) as f:
    time = int(''.join(c for c in f.readline() if c.isdigit()))
    distance = int(''.join(c for c in f.readline() if c.isdigit()))

print(sum(i * (time - i) > distance for i in range(time)))
