import re

with open('data.txt') as f:
    lines = f.readlines()


def clean_crate(lst):
    return [re.findall('[A-Z]', s)[0] for s in lst if len(re.findall('[A-Z]', s)) > 0]


def get_starting_stack(lines):
    stack = []
    for line in lines:
        line = line.replace('\n', '')
        for i in range(0, len(line), 4):
            stack.append(line[i:i+4])
    starting_stack = [clean_crate(stack[x::9]) for x in range(9)]
    starting_stack = [list(reversed(lst)) for lst in starting_stack]
    return starting_stack


def perform_operations(starting_stack, operations, machine):
    operations = [operation.replace('\n', '').split(' ') for operation in operations]
    for operation in operations:
        # Perform operation
        if machine == '9000':
            starting_stack[int(operation[5])-1].extend(list(reversed(starting_stack[int(operation[3])-1][int(operation[1])*-1:])))
        elif machine == '9001':
            starting_stack[int(operation[5])-1].extend(starting_stack[int(operation[3])-1][int(operation[1])*-1:])
        # Remove old data
        del starting_stack[int(operation[3])-1][int(operation[1])*-1:]
    return starting_stack


print(f"{''.join([item[-1] for item in perform_operations(get_starting_stack(lines[:8]), lines[10:], '9000')])}")
print(f"{''.join([item[-1] for item in perform_operations(get_starting_stack(lines[:8]), lines[10:], '9001')])}")