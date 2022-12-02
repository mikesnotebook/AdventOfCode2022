
possible_rounds = [
    "A X",
    "A Y",
    "A Z",
    "B X",
    "B Y",
    "B Z",
    "C X",
    "C Y",
    "C Z"
]

scores = [
    4,
    8,
    3,
    1,
    5,
    9,
    7,
    2,
    6
]

part2_scores = [
    3,
    4,
    8,
    1,
    5,
    9,
    2,
    6,
    7,
]

all_rounds = open("a2_data.txt").read().split('\n')
print('part 1: {}'.format(sum([scores[possible_rounds.index(round)] for round in all_rounds])))
print('part 2: {}'.format(sum([part2_scores[possible_rounds.index(round)] for round in all_rounds])))
