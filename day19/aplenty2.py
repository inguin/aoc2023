#! /usr/bin/python

import sys, re, copy

filename = sys.argv[1] if len(sys.argv) > 1 else "input.txt"

workflows = {}

def parse_workflow(line):
    workflow = []

    name, rules = re.match("(.+){(.+)}", line).groups()
    for rule in rules.split(","):
        if m := re.match("(.+)([<>])(.+):(.+)", rule):
            workflow.append((m[1], m[2], int(m[3]), m[4]))
        else:
            workflow.append((None, None, None, rule))

    workflows[name] = workflow

def count_accepted(parts, state, i):
    if state == "A":
        num = 1
        for begin, end in parts.values():
            num *= (end - begin + 1)
        return num
    elif state == "R":
        return 0

    workflow = workflows[state]
    prop, cmp, value, dest = workflow[i]

    if cmp == '<':
        if parts[prop][1] <= value:
            return count_accepted(parts, dest, 0)
        elif parts[prop][0] < value:
            matched = copy.copy(parts)
            matched[prop] = (parts[prop][0], value - 1)
            notmatched = copy.copy(parts)
            notmatched[prop] = (value, parts[prop][1])
            return count_accepted(matched, dest, 0) + \
                   count_accepted(notmatched, state, i + 1)
        else:
            return count_accepted(parts, state, i + 1)
    elif cmp == '>':
        if parts[prop][0] >= value:
            return count_accepted(parts, dest, 0)
        elif parts[prop][1] > value:
            matched = copy.copy(parts)
            matched[prop] = (value + 1, parts[prop][1])
            notmatched = copy.copy(parts)
            notmatched[prop] = (parts[prop][0], value)
            return count_accepted(matched, dest, 0) + \
                   count_accepted(notmatched, state, i + 1)
        else:
            return count_accepted(parts, state, i + 1)
    else:
        return count_accepted(parts, dest, 0)

with open(filename) as f:
    while line := f.readline().strip():
        parse_workflow(line)

all_parts = { "x": (1, 4000), "m": (1, 4000), "a": (1, 4000), "s": (1, 4000) }
print(count_accepted(all_parts, "in", 0))
