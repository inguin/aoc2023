#! /bin/python

result = 0

values = {
        "0": 0, "zero": 0,
        "1": 1, "one": 1,
        "2": 2, "two": 2,
        "3": 3, "three": 3,
        "4": 4, "four": 4,
        "5": 5, "five": 5,
        "6": 6, "six": 6,
        "7": 7, "seven": 7,
        "8": 8, "eight": 8,
        "9": 9, "nine": 9
}

with open("input.txt") as file:
    for line in file:
        first = (len(line), None)
        last = (-1, None)

        for word, value in values.items():
            if (pos := line.find(word)) >= 0:
                if pos < first[0]:
                    first = (pos, value)
            if (pos := line.rfind(word)) >= 0:
                if pos > last[0]:
                    last = (pos, value)

        result += 10 * first[1] + last[1]

print(result)
