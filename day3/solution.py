import string
from functools import reduce

with open('data.txt') as f:
    lines = f.readlines()


def priority(elem):
    # Lowercase item types a through z have priorities 1 through 26.
    # Uppercase item types A through Z have priorities 27 through 52.
    lower = string.ascii_lowercase.index(elem.lower()) + 1
    return lower if elem.islower() else lower + 26


# PART 1
prio_one = 0
for line in lines:
    line = line.replace('\n', '')
    assert len(line) % 2 == 0
    # Split in half
    compartment_one, compartment_two = [i for i in line[:int(len(line)/2)]], [j for j in line[int(len(line)/2):]]
    # Find intersecting elems
    intersection = list(set(compartment_one).intersection(set(compartment_two)))
    assert len(intersection) == 1
    # Find priority
    prio_one += priority(intersection[0])

print(prio_one)

# Part 2
prio_two = 0
for k, line in enumerate(lines[::3]):
    # Find badge
    set_one, set_two, set_three = [l for l in lines[k*3].replace('\n', '')], [m for m in lines[k*3+1].replace('\n', '')], [n for n in lines[k*3+2].replace('\n', '')]
    intersection = list(reduce(set.intersection, [set(item) for item in [set_one, set_two, set_three] ]))
    assert len(intersection) == 1
    # Find priority
    prio_two += priority(intersection[0])

print(prio_two)
