
PATH = 'day09/input.txt'
# PATH = 'day09/test.txt'
# PATH = 'day09/test2.txt'

def extrapolated_value(dataset):
    i = 0
    while(any(dataset[i])):
        new = []
        for j in range(0, len(dataset[i])-1):
            # if(len(dataset[i]) == 2):
            #     new.append(0)
            # else:
            new.append((dataset[i][j+1]-dataset[i][j]))
        dataset[i+1] = new[:]
        i += 1
    # print("dataset last line:")
    # print(list(dataset.values())[-1])
    # print("calculate extrapolated value now...")
    #let's calculate extrapolated value:
    #we add a wero at first:
    list(dataset.values())[-1].append(0)
    for i in range(len(dataset)-1, 0, -1):
        offset = dataset[i][-1]
        # print(f"We add {offset} to {dataset[i-1][-1]}: {dataset[i-1][-1]+offset}")
        dataset[i-1].append(dataset[i-1][-1]+offset)
    # print("dataset:")
    # print(dataset)
    # print("---------")
    return dataset[0][-1]

input = open(PATH, 'r').read().rstrip().split("\n")

result = []
result2 = []
for line in input:
    dataset = {}
    dataset2 = {}
    dataset[0] = [int(x) for x in line.split(" ")]
    dataset2[0] = dataset[0].copy()
    dataset2[0].reverse()
    print(dataset2)

    result.append(extrapolated_value(dataset))
    result2.append(extrapolated_value(dataset2))

# print(result)
print(f"part1 {sum(result)}")
print(f"part2 {sum(result2)}")

#1970867146 is too high
#1972898376 is too high
#1972072521
#1969958228 is too low
#1969958987