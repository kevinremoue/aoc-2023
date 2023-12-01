input = open('day01/input.txt', 'r').read().rstrip().split("\n")
# input = open('day01/test.txt', 'r').read().rstrip().split("\n")
result = []

for entry in input:
    couple = ""
    digits = [i for i in entry if i.isdigit()]
    if len(digits) > 1:
        couple = digits[0]+ digits[len(digits)-1]
    elif len(digits) == 1:
        couple = digits[0]+digits[0]
    result.append(int(couple))

print(sum(result))
