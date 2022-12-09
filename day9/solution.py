with open('data.txt') as f:
    lines = f.readlines()

directions = {
    'L': (-1, 0), 
    'R': (1, 0),
    'U': (0, 1),
    'D': (0, -1)
}

def visited_places(lines, ln):
    length = ln
    xs, ys = [0] * length, [0] * length
    visited = [(0, 0)]

    for line in lines:
        (x,y), steps = directions[line.split()[0]], int(line.split()[1])

        for _ in range(steps):
            xs[0] += x
            ys[0] += y
            for i in range(length - 1):
                dx = xs[i + 1] - xs[i]
                dy = ys[i + 1] - ys[i]
                if abs(dx) == 2 or abs(dy) == 2:
                    xs[i + 1] = xs[i] + int(dx / 2)
                    ys[i + 1] = ys[i] + int(dy / 2)
            visited.append( (xs[-1], ys[-1]) )

    return len(set(visited))

print(visited_places(lines, 2))
print(visited_places(lines, 10))
