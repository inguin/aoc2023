#! /usr/bin/python

import re, sys

def map_seeds(seeds, mappings):
    new_seeds = []
    while seeds:
        first, seed_count = seeds.pop()
        for (dest, source, map_count) in mappings:
            overlap_first = max(first, source)
            overlap_last = min(first + seed_count, source + map_count)
            if overlap_last > overlap_first:
                new_seeds.append((overlap_first - source + dest, overlap_last - overlap_first))
                if first < overlap_first:
                    seeds.append((first, overlap_first - first))
                if first + seed_count > overlap_last:
                    seeds.append((overlap_last, first + seed_count - overlap_last))
                break
        else:
            new_seeds.append((first, seed_count))
    return new_seeds

filename = sys.argv[1] if len(sys.argv) > 1 else "input.txt"

with open(filename) as f:
    tokens = [ int(token) for token in re.findall('\d+', f.readline()) ]
    tokens.reverse()
    seeds = []
    while tokens:
        seeds.append((tokens.pop(), tokens.pop()))
    print(seeds)

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
print(seeds)
print(min(seeds))
