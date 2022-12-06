with open('data.txt') as f:
    lines = f.readlines()

print(f"{[next(i for i, char in enumerate(lines[0]) if len(set([j for j in lines[0][i-n:i]])) == n) for n in (4,14)]}")
