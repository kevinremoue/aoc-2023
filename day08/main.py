import re

PATH = 'day08/input.txt'
# PATH = 'day08/test2.txt'

LETTER_TO_INDEX = {'L': 0, 'R': 1}

input = open(PATH, 'r').read().rstrip().split("\n")

#Get instructions
instructions = [c for c in input.pop(0)]

#Get Elements
nodes = {}
input.pop(0)

for line in input:
    node = []
    match = re.findall(r'[A-Z]{3}', line)
    node.append(match[1])
    node.append(match[2])
    nodes[match[0]] = node
print(nodes)

found = False
steps = 0
#first one
current = 'AAA'
#Process
while not found:
    for instruction in instructions:
        print(f"Current is {current}, {nodes.get(current)}")
        current = nodes[current][LETTER_TO_INDEX[instruction]]
        steps +=1
        if current == 'ZZZ':
            found = True
            print(steps)
            break
