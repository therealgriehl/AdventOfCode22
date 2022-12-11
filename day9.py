### Advent of Code - Day 9 ###

import numpy as np
from copy import deepcopy

# Part One - (off by 5)

instructions = []
with open(r'C:\Users\rngl\VSCode\AdventOfCode22\input\9_1.txt') as file_in:
    for line in file_in:
        line = line.rstrip()
        line = line.split()
        instructions.append(line)

print(instructions)

positions = {}
pos_head = [0,0]
pos_tail = [0,0]
direction = {'R': 1, 'L': -1, 'U': -1, 'D': 1}

for i,instruct in enumerate(instructions):
    for step in range(int(instruct[1])):

        old_pos_head = deepcopy(pos_head)

        if instruct[0] == 'L' or instruct[0] == 'R':
            pos_head[0] = pos_head[0] + direction[instruct[0]]
        if instruct[0] == 'U' or instruct[0] == 'D':
            pos_head[1] = pos_head[1] + direction[instruct[0]]

        diff_x = abs(pos_head[0] - pos_tail[0]) 
        diff_y = abs(pos_head[1] - pos_tail[1])

        if diff_x > 1 or diff_y > 1:
            pos_tail[0] = old_pos_head[0]
            pos_tail[1] = old_pos_head[1]
            
        
        temp_pos = str(pos_tail[0]) + str(pos_tail[1])
        positions[temp_pos] = 0

print(len(positions))





ds = {
    "R": np.array((1, 0)),
    "L": np.array((-1, 0)),
    "U": np.array((0, 1)),
    "D": np.array((0, -1)),
}

# Part Two

k = np.zeros((10,2))
visited = set()
for line in instructions:
    d = line[0]
    n = line[1]
    for i in range(int(n)):
        k[0] += ds[d]
        for j in range(1,10):
            if np.max(np.abs(k[j] - k[j-1])) > 1: # L0 norm
                k[j] += np.sign(k[j-1] - k[j]) # move up to 1 step in each axis
        visited.add(tuple(k[-1]))

print(len(visited))