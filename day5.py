### Advent of Code ###
    ### Day 5 ###

import re
import copy

# Part One

with open(r'AdventOfCode22\input\5_1.txt') as file_in:
    towers = [[] for _ in range(9)]
    counter = 0
    for line in file_in:
        if '1' in line:
            break
        line.strip('\n')
        crates = re.findall('....?', line)
        print(crates)
        for i in range(len(crates)):
            if crates[i].isupper():
                crates[i] = re.sub(r'[^a-zA-Z]', '', crates[i])
                towers[i].append(crates[i])

# save original for part 2
towers2 = copy.deepcopy(towers)

print(towers)

with open(r'AdventOfCode22\input\5_1.txt') as file_in:
    instructions = []
    counter = 0
    lines = 0
    for line in file_in:
        lines += 1
        if lines < 11:
            continue
        instructions.append(list(map(int, re.findall(r'\d+', line))))


for i in range(len(instructions)):
    amount = instructions[i][0]
    start = instructions[i][1] -1
    end = instructions[i][2] - 1

    for j in range(amount):

        element = towers[start][0]
        towers[end].insert(0, element)
        towers[start].pop(0)

print(towers)

tops = [item[0] for item in towers]
tops = ''.join(tops)
print(tops)

# Part Two

for i in range(len(instructions)):
    amount = instructions[i][0]
    start = instructions[i][1] -1
    end = instructions[i][2] - 1

    elements = towers2[start][0:(amount)]
    towers2[end][:0] = elements
    del towers2[start][0:amount]
        
print(towers2)

tops2 = [item[0] for item in towers2]
tops2 = ''.join(tops2)
print(tops2)