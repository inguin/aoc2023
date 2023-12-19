#! /usr/bin/python

import sys, re

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

def parse_part(line):
    part = {}
    for token in line.split(","):
        name, value = token.split("=")
        part[name] = int(value)
    return part

def process_part(part):
    workflow = workflows["in"]
    i = 0

    while True:
        prop, cmp, value, dest = workflow[i]
        if (cmp == '<' and part[prop] < value) or \
           (cmp == '>' and part[prop] > value) or \
           prop is None:
            if dest in workflows:
                workflow = workflows[dest]
                i = 0
            else:
                return dest == 'A'
        else:
            i = i + 1

total = 0

with open(filename) as f:
    while line := f.readline().strip():
        parse_workflow(line)

    for line in f:
        part = parse_part(line.strip("{}\n"))
        accepted = process_part(part)
        print(part, "ACCEPT" if accepted else "REJECT")
        if accepted:
            total += sum(part.values())

print(total)
