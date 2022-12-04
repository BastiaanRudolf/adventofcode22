with open('data.txt') as f:
    lines = f.readlines()


def get_ranges(line):
    line = line.replace('\n','')
    nrs1, nrs2 = line.split(',')[0].split('-'), line.split(',')[1].split('-')
    return list(range(int(nrs1[0]), int(nrs1[1]) +1)), list(range(int(nrs2[0]), int(nrs2[1]) +1))


def part_1(line):
    range1, range2 = get_ranges(line)
    return 1 if sorted(list(set(range1) & set(range2))) == range1 else 1 if sorted(list(set(range1) & set(range2))) == range2 else 0


def part_2(line):
    range1, range2 = get_ranges(line)
    return 1 if len(list(set(range1) & set(range2))) > 0 else 0


# Part 1: Fully contained sections
print(f"Total overlaps: {sum(list(map(lambda x: part_1(x), lines)))}")
print(f"Partly overlaps: {sum(list(map(lambda x: part_2(x), lines)))}")