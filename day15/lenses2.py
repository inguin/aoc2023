#! /usr/bin/python

import sys, re

def hash(s):
    result = 0
    for c in s.encode("ascii"):
        result = 17 * (result + c) % 256
    return result

filename = sys.argv[1] if len(sys.argv) > 1 else "input.txt"
line = open(filename).readline().strip()

boxes = [ [] for _ in range(256) ]

for token in line.split(","):
    lens, op, focal = re.match("(.+)([-=])([0-9]*)", token).groups()
    box = hash(lens)
    if op == "-":
        boxes[box] = [ item for item in boxes[box] if item[0] != lens ]
    else:
        for item in boxes[box]:
            if item[0] == lens:
                item[1] = int(focal)
                break
        else:
            boxes[box].append([lens, int(focal)])

total = sum(box * slot * focal
            for box, lenses in enumerate(boxes, 1)
            for slot, (_, focal) in enumerate(lenses, 1))

print(total)
