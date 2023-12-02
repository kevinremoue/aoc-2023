def is_game_valid(string):
    number = game.split(":")[0].split(" ")[1]
    grabs = game.split(":")[1].split(";")
    for grab in grabs:
        for couple in grab.split(","):
            nb = int(couple.lstrip().split(" ")[0])
            color = couple.lstrip().split(" ")[1]
            if color == "blue":
                if nb > NB_BLUE:
                    return 0
            elif color == "red":
                if nb > NB_RED:
                    return 0
            elif color == "green":
                if nb > NB_GREEN:
                    return 0
    print(f"Game {number} is valid")            
    return int(number)

def mini_set_of_cubes(string):
    number = game.split(":")[0].split(" ")[1]
    grabs = game.split(":")[1].split(";")
    min_blue = 0
    min_green = 0
    min_red = 0
    for grab in grabs:
        for couple in grab.split(","):
            nb = int(couple.lstrip().split(" ")[0])
            color = couple.lstrip().split(" ")[1]
            if color == "blue":
                if nb > min_blue:
                    min_blue = nb
            elif color == "red":
                if nb > min_red:
                    min_red = nb
            elif color == "green":
                if nb > min_green:
                    min_green = nb
    return min_blue*min_red*min_green

input = open('day02/input.txt', 'r').read().rstrip().split("\n")
# input = open('day02/test.txt', 'r').read().rstrip().split("\n")

#part1
result1 = 0
#part2
result2 = 0

NB_RED = 12
NB_GREEN = 13
NB_BLUE = 14


for game in input:
    result1 = result1 + is_game_valid(game)
    result2 = result2 + mini_set_of_cubes(game)

print(result1)
print(result2)

