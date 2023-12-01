import re

digits = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
word_to_digit = {'zero': 0, 'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5, 'six': 6, 'seven': 7, 'eight': 8, 'nine': 9}

def find_first_digit(input):
    current_word = ""
    for char in input:
        if char.isdigit():
            return int(char)
        else:
            current_word += char
            if current_word in word_to_digit:
                return (word_to_digit.get(current_word))
            if any(digit in current_word for digit in digits):
                digit = re.findall("|".join(digits), current_word)
                return (word_to_digit.get(str(digit[0])))

def find_last_digit(input):
    current_word = ""
    for char in reversed(input):
        if char.isdigit():
            return int(char)
        else:
            current_word = char + current_word
            if current_word in word_to_digit:
                return (word_to_digit.get(current_word))
            if any(digit in current_word for digit in digits):
                digit = re.findall("|".join(digits), current_word)
                return (word_to_digit.get(str(digit[0])))

input = open('day01/part2/input.txt', 'r').read().rstrip().split("\n")
# input = open('day01/part2/test.txt', 'r').read().rstrip().split("\n")

result = []

for entry in input:
    first_digit = find_first_digit(entry)
    last_digit = find_last_digit(entry)
    couple = str(first_digit)+str(last_digit)
    result.append((int(couple)))

print(sum(result))
