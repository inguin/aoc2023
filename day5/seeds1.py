#! /usr/bin/python

import re, sys

def map_seeds(seeds, mappings):
    new_seeds = []
    for seed in seeds:
        for (dest, source, count) in mappings:
            if seed in range(source, source + count):
                new_seeds.append(dest + seed - source)
                break
        else:
            new_seeds.append(seed)
    return new_seeds

filename = sys.argv[1] if len(sys.argv) > 1 else "input.txt"

with open(filename) as f:
    seeds = [ int(token) for token in re.findall('\d+', f.readline()) ]

    mappings = []
    for line in f:
        if line.endswith("map:\n"):
            seeds = map_seeds(seeds, mappings)
            print(seeds)
            mappings = []

        tokens = [ int(token) for token in re.findall('\d+', line) ]
        if len(tokens) == 3:
            mappings.append((*tokens,))

seeds = map_seeds(seeds, mappings)
print(min(seeds))
