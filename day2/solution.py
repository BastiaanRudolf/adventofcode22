from collections import OrderedDict

shapes = {
    'A': 'rock',
    'B': 'paper',
    'C': 'scissors',
    'X': 'rock',
    'Y': 'paper',
    'Z': 'scissors'
}

ordered_dict = OrderedDict([
    ('rock',     [3, 0, 6]),
    ('paper',    [6, 3, 0]),
    ('scissors', [0, 6, 3])
])

# PART 1
def calculate_score_part_1(opponent, you):
    game_score = ordered_dict[shapes[you]][list(ordered_dict.keys()).index(shapes[opponent])]
    item_score = list(ordered_dict.keys()).index(shapes[you]) + 1
    return game_score + item_score


# PART 2
def calculate_score_part_2(opponent, you):
    # Inverse
    idx = 6 if you == 'X' else 3 if you == 'Y' else 0
    game_score = 0 if you == 'X' else 3 if you == 'Y' else 6
    item_score = ordered_dict[shapes[opponent]].index(idx) + 1
    return game_score + item_score


with open('data.txt') as f:
    lines = f.readlines()

score_1 = 0
score_2 = 0
for line in lines:
    opponent = line.replace('\n', '').split(' ')[0]
    you = line.replace('\n', '').split(' ')[1]
    score_1 += calculate_score_part_1(opponent, you)
    score_2 += calculate_score_part_2(opponent, you)
print(score_1)
print(score_2)