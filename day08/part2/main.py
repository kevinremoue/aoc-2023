import re
import time 

def is_finish(currents):
    result = True
    for current in currents:
        result = result & bool(re.search(r'([A-Z0-9]{2}[Z])', current))
        if bool(re.search(r'([A-Z0-9]{2}[Z])', current)):
            print(f"Z found in {current}")
    return result


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

# print(nodes)
# print("--------")
print(currents)

found = False
steps = 0
currents = currents[0:1]
print(currents)

#Process
while True:
    # time.sleep(1)
    for instruction in instructions:
        currents = [nodes[current][LETTER_TO_INDEX[instruction]] for current in currents]
        steps +=1
        if is_finish(currents):
            found = True
            print(steps)
            

