#! /usr/bin/python

import sys, re, math

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

def reset():
    for module in modules.values():
        module.state = False
        for iname in module.inputs:
            module.inputs[iname] = False

def simulate(monitor_name):
    events = [ ('button', 'broadcaster', False) ]
    high_events = 0
    low_events = 0

    while events:
        source, name, level = events[0]
        events = events[1:]

        module = modules[name]
        result = module.pulse(source, level)

        if result != None:
            if name == monitor_name:
                if result:
                    high_events += 1
                else:
                    low_events += 1

            for oname in module.outputs:
                events.append((name, oname, result))

    return high_events, low_events

def print_tree(name, indent, limit, visited):
    module = modules[name]
    print(f"{indent}{name}: {module.op}")
    if limit > 0:
        for iname in module.inputs:
            if iname in visited:
                print(f"{indent}  {iname} (feedback)")
            else:
                print_tree(iname, indent + "  ", limit - 1, visited + [iname])

def collect_inputs(name, inputs):
    for iname in modules[name].inputs:
        if iname != "button" and not iname in inputs:
            inputs.add(iname)
            collect_inputs(iname, inputs)

def analyze(name):
    inputs = set()
    inputs.add(name)
    collect_inputs(name, inputs)
    inputs = sorted(inputs)

    reset()
    cache = []

    print(f"{name}:")
    while True:
        istates = [ modules[iname].state for iname in inputs ]
        if istates in cache:
            break
        cache.append(istates)

        high_events, low_events = simulate(name)
        if high_events:
            print(f" - {len(cache)}: {high_events} high event(s)")

    print(f" - repeat after {len(cache)} cycles")
    return len(cache)

filename = sys.argv[1] if len(sys.argv) > 1 else "input.txt"

with open(filename) as f:
    for line in f:
        parse_module(line)

print_tree("rx", "", 4, [])

# "rx" is a NAND conjunction of the following signals, which happen to emit
# a single high pulse in the next-to-last cycle of their periodicity.
signals = [ "rd", "bt", "fv", "pr" ]

cycles = []
for signal in signals:
    cycles.append(analyze(signal) - 1)

print(math.lcm(*cycles))
