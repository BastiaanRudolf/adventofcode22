with open('data.txt') as f:
    lines = f.readlines()

string = ''.join(lines).split('\n\n')
total_calories_per_elf = list(map(lambda x: sum([int(calories) for calories in x.split('\n')]), string))

print(f"max calories: {max(total_calories_per_elf)}")
print(f"sum of top three: {sum(sorted(total_calories_per_elf)[-3:])}")