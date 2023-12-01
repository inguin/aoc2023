#! /bin/python

result = 0

with open("input.txt") as file:
    for line in file:
        digits = [ c for c in line if c.isdigit() ]
        result += int(digits[0] + digits[-1])

print(result)
