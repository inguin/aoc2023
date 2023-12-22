#! /usr/bin/python

import sys, re

filename = sys.argv[1] if len(sys.argv) > 1 else "input.txt"

class Brick():
    def __init__(self, n, line):
        coords = list(map(int, re.findall("\d+", line)))
        self.n = n
        self.x1 = coords[0]
        self.y1 = coords[1]
        self.z1 = coords[2]
        self.x2 = coords[3]
        self.y2 = coords[4]
        self.z2 = coords[5]
        assert(self.x1 <= self.x2)
        assert(self.y1 <= self.y2)
        assert(self.z1 <= self.z2)
        self.supports = set()
        self.supported_by = set()

    def __repr__(self):
        return f"{self.n}: {self.x1},{self.y1},{self.z1}~{self.x2},{self.y2},{self.z2}"

bricks = []

with open(filename) as f:
    for n, line in enumerate(f):
        bricks.append(Brick(n, line))

stacks = {}

for brick in sorted(bricks, key=lambda b: b.z1):
    top_z = 0
    for x in range(brick.x1, brick.x2 + 1):
        for y in range(brick.y1, brick.y2 + 1):
            if (x, y) in stacks:
                top = stacks[(x, y)][-1]
                stacks[(x, y)].append(brick)
                if top.z2 > top_z:
                    brick.supported_by = set([top])
                    top_z = top.z2
                elif top.z2 == top_z:
                    brick.supported_by.add(top)
            else:
                stacks[(x, y)] = [brick]
    if (diff := brick.z1 - top_z - 1) > 0:
        print(f"Brick {brick.n} falls {diff} tiles.")
        brick.z1 -= diff
        brick.z2 -= diff
    print(f"Brick {brick.n} is supported by {len(brick.supported_by)} bricks: {[b.n for b in brick.supported_by]}.")
    for other in brick.supported_by:
        other.supports.add(brick)

print(bricks)

result = 0

for brick in bricks:
    print(f"Brick {brick.n} supports {len(brick.supports)} bricks: {[b.n for b in brick.supports]}.")
    if all(len(other.supported_by) > 1 for other in brick.supports):
        print(f"Brick {brick.n} is safe to remove.")
        result += 1

print(f"{result} bricks could be disintegrated.")
