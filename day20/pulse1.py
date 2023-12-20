#! /usr/bin/python

import sys, re

class Module:
    def __init__(self):
        self.op = '?'
        self.outputs = []
        self.inputs = {}
        self.state = False

    def __str__(self):
        return f"{self.op}({','.join(self.inputs.keys())}) -> {','.join(self.outputs)}"

    def pulse(self, iname, level):
        self.inputs[iname] = level
        if self.op == '*':
            self.state = level
            return self.state
        elif self.op == '&':
            self.state = not all(self.inputs.values())
            return self.state
        elif self.op == '%':
            if not level:
                self.state = not self.state
                return self.state
        return None

modules = {}

def parse_module(line):
    name, outputs = line.strip().split(" -> ")
    outputs = outputs.split(", ")

    if name == "broadcaster":
        op = '*'
    else:
        op = name[0]
        name = name[1:]

    if name not in modules:
        modules[name] = Module()

    modules[name].op = op
    modules[name].outputs = outputs

    for output in outputs:
        if output not in modules:
            modules[output] = Module()

        modules[output].inputs[name] = False

def simulate():
    events = [ ('button', 'broadcaster', False) ]
    output_events = []
    low_events = 0
    high_events = 0

    while events:
        source, name, level = events[0]
        print(f"{source} -{'high' if level else 'low'}-> {name}")
        events = events[1:]

        if level:
            high_events += 1
        else:
            low_events += 1

        module = modules[name]
        result = module.pulse(source, level)

        if result != None:
            for oname in module.outputs:
                events.append((name, oname, result))

    print(f"{high_events} high events, {low_events} low events")
    return high_events, low_events

filename = sys.argv[1] if len(sys.argv) > 1 else "input.txt"

with open(filename) as f:
    for line in f:
        parse_module(line)

for name, module in modules.items():
    print(f"{name}: {module}")

high_events = 0
low_events = 0

for _ in range(1000):
    h, l = simulate()
    high_events += h
    low_events += l

print(f"{high_events} high * {low_events} low = {high_events * low_events}")
