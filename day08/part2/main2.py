import re
import time 

PATH = 'day08/input.txt'
# PATH = 'day08/part2/test.txt'

LETTER_TO_INDEX = {'L': 0, 'R': 1}

input = open(PATH, 'r').read().rstrip().split("\n")

#Get instructions
instructions = [c for c in input.pop(0)]

#Get Elements
nodes = {}
input.pop(0)

currents = []

for line in input:
    node = []
    match = re.findall(r'[A-Z0-9]{2}[A-Z]', line)
    node.append(match[1])
    node.append(match[2])
    nodes[match[0]] = node
    if re.match(r'([A-Z0-9]{2}[A])', match[0]):
        currents.append(match[0])

found = False
steps = 0
currents = currents[:1]
print(currents)

#Process
while True:
    for instruction in instructions:
        for current in currents:
            current = nodes[current][LETTER_TO_INDEX[instruction]]
            steps +=1
            if current[-1] == 'Z':
                print("found")
                found = True
                print(steps)