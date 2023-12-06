PATH = 'day06/input.txt'
# PATH = 'day06/test.txt'

def calculate_ways(time, distance):
    ways = 0
    #for sure first and last value wont do it
    for i in range(time-1, 1, -1):
        # print(f"holding the button for {i}")
        time_left = time - i
        speed = i
        distance_calculated = time_left*speed
        # print(f">>time left is {time_left} for a speed of {speed} so it will travel {distance_calculated}")
        if distance_calculated>distance:
            ways += 1
    return ways


input = open(PATH, 'r').read().rstrip().split("\n")
time = [int(x) for x in input[0].split(" ") if x.isdigit()]
distance = [int(x) for x in input[1].split(" ") if x.isdigit()]

print(time)
print(distance)

results = []

for i in range(len(time)):
    ways = calculate_ways(time[i], distance[i])
    results.append(ways)

print(results)
total = 1
for result in results:
    total = total*result
print(total)