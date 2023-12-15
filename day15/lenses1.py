#! /usr/bin/python

import sys, re

def hash(s):
    result = 0
    for c in s.encode("ascii"):
        result = 17 * (result + c) % 256
    return result

filename = sys.argv[1] if len(sys.argv) > 1 else "input.txt"
line = open(filename).readline().strip()

print(sum(hash(token) for token in line.split(",")))
