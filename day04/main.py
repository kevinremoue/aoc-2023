import copy
import re

_RE_COMBINE_WHITESPACE = re.compile(r"\s+")

def calculate_score(result):
    score = 0
    multiplier = 1
    for elt in result:
        score=multiplier
        multiplier *= 2
    return score


def calculate_cards_combi(current_card, result, cards):
    new_card = 0
    for card in result:
        cards[current_card+new_card] += 1
        new_card +=1
    return cards


input = open('day04/input.txt', 'r').read().rstrip().split("\n")
# input = open('day04/test.txt', 'r').read().rstrip().split("\n")
score = 0 

nb_cards = sum(1 for _ in input)
list_of_cards = [0] * nb_cards
ref_combi = []

for line in input:
    line = _RE_COMBINE_WHITESPACE.sub(" ", line).strip()
    print(line)
    print(line.split(":")[0].split(" "))
    current_card = int(line.split(":")[0].split(" ")[1])
    winning_cards = set(line.split(":")[1].split("|")[0].strip().split(" "))
    cards = set(line.split(":")[1].split("|")[1].strip().split(" "))
    result = cards.intersection(winning_cards)
    #part1
    score += calculate_score(result)

    #part2
    list_of_cards = calculate_cards_combi(current_card, result, list_of_cards)
    ref_combi.append(list_of_cards)
    list_of_cards = [0] * nb_cards

#part1
print(f"Part1: {score}")

#part2
#process combi
copies = [0] * nb_cards
print(ref_combi)
cards = [0] * nb_cards


for i in range(0, nb_cards):
    print(f"Getting copies for cards {i+1}")
    cards[i] += 1
    copies = [x + y for x, y in zip(copies, ref_combi[i])]

    print(f">>is there copies for card {i+1} ? -> {copies[i]}")
    for j in range(0, copies[i]):
        cards[i] += 1
        copies = [x + y for x, y in zip(copies, ref_combi[i])]
    
    print(f"current cards: {cards}")

#score part 2

score2 = sum(cards)
print(f"Part2: {score2}")
