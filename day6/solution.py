with open('data.txt') as f:
    lines = f.readlines()


def comb_is_unique(comb, min_length):
    return True if len(set([i for i in comb])) == min_length else False


print(f"Start of packet marker: {[i for i, char in enumerate(lines[0]) if comb_is_unique(lines[0][i-4:i], 4)][0]}")
print(f"Start of message marker: {[i for i, char in enumerate(lines[0]) if comb_is_unique(lines[0][i-14:i], 14)][0]}")
