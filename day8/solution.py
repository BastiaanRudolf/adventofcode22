with open('data.txt') as f:
    lines = f.readlines()

trees = [[*line.replace('\n', '')] for line in lines]


def get_visibility(trees, x, y):
    height = trees[y][x]
    left, right = trees[y][:x], trees[y][x+1:]
    up, down = [el[x] for el in trees][y+1:], [el[x] for el in trees][:y]

    if len(left) == 0 or len(right) == 0 or len(up) == 0 or len(down) == 0:
        return 1
    elif height > max(left) or height > max(right) or height > max(up) or height > max(down):
        return 1
    else:
        return 0


def calc(arr, height):
    score = 0
    for h in arr:
        if h < height:
            score += 1
        elif h == height:
            score += 1
            break
        else:
            break
    return score


def scenic_score(trees, x, y):
    height = trees[y][x]
    left, right = list(reversed(trees[y][:x])), trees[y][x+1:]
    down, up = [el[x] for el in trees][y+1:], list(reversed([el[x] for el in trees][:y]))
    scenic_left, scenic_right = calc(left, height), calc(right, height)
    scenic_up, scenic_down = calc(up, height), calc(down, height)

    return scenic_left * scenic_right * scenic_up * scenic_down


print(sum([get_visibility(trees, s, t) for s in range(len(trees)) for t in range(len(trees[0]))]))
print(max([scenic_score(trees, s, t) for s in range(len(trees)) for t in range(len(trees[0]))]))
