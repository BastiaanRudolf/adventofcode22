with open('data.txt') as f:
    lines = f.readlines()

print(f"Start of packet marker: {[i for i, char in enumerate(lines[0]) if len(set([j for j in lines[0][i-4:i]])) == 4][0]}")
print(f"Start of message marker: {[i for i, char in enumerate(lines[0]) if len(set([j for j in lines[0][i-14:i]])) == 14][0]}")
