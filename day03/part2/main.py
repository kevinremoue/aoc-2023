RESULT = 0
COORD_VERIFIED = [] #y-x
SYMBOLS = "*"
MATRIX = []
YMAX = 0
XMAX = 0

def is_symbol(char):
    if char in SYMBOLS:
        return True
    else:
        return False

def get_number(x,y):
    str_coord = str(y) + "-" + str(x)
    number = ""
    #if not checked before and a number we look further:
    if str_coord not in COORD_VERIFIED:
        if MATRIX[y][x].isdigit():
            COORD_VERIFIED.append(str_coord)
            number = MATRIX[y][x]
            #check x+1:
            if MATRIX[y][x+1].isdigit():
                str_coord = str(y) + "-" + str(x+1)
                if str_coord not in COORD_VERIFIED:
                    COORD_VERIFIED.append(str_coord)
                    number = number + MATRIX[y][x+1]
                    #check x+2:
                    if x+2 <= XMAX:
                        str_coord = str(y) + "-" + str(x+2)
                        if str_coord not in COORD_VERIFIED:
                            if MATRIX[y][x+2].isdigit():
                                COORD_VERIFIED.append(str_coord)
                                number = number+MATRIX[y][x+2]

            #check x-1:
            if MATRIX[y][x-1].isdigit():
                str_coord = str(y) + "-" + str(x-1)
                if str_coord not in COORD_VERIFIED:
                    COORD_VERIFIED.append(str_coord)
                    number = MATRIX[y][x-1]+number
                    #check x-2:
                    if x-2 >= 0:
                        str_coord = str(y) + "-" + str(x-2)
                        if str_coord not in COORD_VERIFIED:
                            if MATRIX[y][x-2].isdigit():
                                COORD_VERIFIED.append(str_coord)
                                number = MATRIX[y][x-2]+number    
    if number == "":
        return 0
    else:
        return int(number)

def calculate_part2(gears):
    global RESULT
    gear_total = 1
    #cleaning 0 as they do not mean anything
    if len(gears) > 0:
        gears = [i for i in gears if i != 0]

    #a gear ratio is only 2 values
    if len(gears) > 1 and len(gears) < 3:
        for gear in gears:
            gear_total = gear_total * gear
        RESULT += gear_total

def process_parts(x,y):
    gear = []
    if MATRIX[y-1][x-1].isdigit():
        gear.append(get_number(x-1,y-1))
    if MATRIX[y-1][x].isdigit():
        gear.append(get_number(x,y-1))
    if MATRIX[y-1][x+1].isdigit():
        gear.append(get_number(x+1,y-1))
    if MATRIX[y][x+1].isdigit():
        gear.append(get_number(x+1,y))
    if MATRIX[y][x-1].isdigit():
        gear.append(get_number(x-1,y))
    if MATRIX[y+1][x+1].isdigit():
        gear.append(get_number(x+1,y+1))
    if MATRIX[y+1][x].isdigit():
        gear.append(get_number(x,y+1))
    if MATRIX[y+1][x-1].isdigit():
        gear.append(get_number(x-1,y+1))
    calculate_part2(gear)
    return 0

input = open("day03/input.txt", "r").read().rstrip().split("\n")
# input = open("day03/test.txt", "r").read().rstrip().split("\n")

YMAX = len(input)
for y in range(0, len(input)):
    line = input[y]
    row = []
    for x in range(0, len(line)):
        row.append(line[x])
    XMAX = len(row)
    MATRIX.append(row)

for y in range(1, YMAX-1):
    for x in range(1, XMAX-1):
        if is_symbol(MATRIX[y][x]):
            process_parts(x,y)

print(RESULT)