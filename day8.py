### Advent of Code ###
### Day 8 ###

import numpy as np

# Part One

length = 0
width = 0
rows = []

with open(r'C:\Users\rngl\VSCode\AdventOfCode22\input\8_1.txt') as file_in:
    for line in file_in:
        line = line.rstrip()
        length += 1
        if length == 1:
            width = len(line)
        
        rows.append(list(map(int,list(line))))

grid = np.array(rows)

print(grid)

visibles = np.zeros((length, width))


# Left to Right
for x in range(width):
    max_x = -1
    for y in range(length):
        if grid[x,y] > max_x:
            visibles[x,y] = 1
            max_x = grid[x,y]
        

# Right to Left
for x in range(width-1, -1, -1):
    max_x = -1
    for y in range(length-1, -1 , -1):
        if grid[x,y] > max_x:
            visibles[x,y] = 1
            max_x = grid[x,y]

# Top to Bottom
for x in range(width):
    max_y = -1
    for y in range(length):
        if grid[y,x] > max_y:
            visibles[y,x] = 1
            max_y = grid[y,x]

# Bottom to Top
for x in range(width-1, -1, -1):
    max_y = -1
    for y in range(length-1, -1 , -1):
        if grid[y,x] > max_y:
            visibles[y,x] = 1
            max_y = grid[y,x]


print(visibles.sum())
print(visibles.size)

# Part Two
highest_scenic_score = 0

for x, row in enumerate(rows):
    for y, tree in enumerate(rows[x]):
        scenic_score = [0,0,0,0]

        for left in range(y-1, -1, -1):
            scenic_score[0] += 1
            if rows[x][left] >= rows[x][y]:
                break
        for right in range(y+1, len(rows[x])):
            scenic_score[1] += 1
            if rows[x][right] >= rows[x][y]:
                break
        for up in range(x-1, -1, -1):
            scenic_score[2] += 1
            if rows[up][y] >= rows[x][y]:
                break
        for down in range(x+1, len(rows)):
            scenic_score[3] += 1
            if rows[down][y] >= rows[x][y]:
                break

        current_score = scenic_score[0] * scenic_score[1] * scenic_score[2] * scenic_score[3]

        if current_score > highest_scenic_score:
            highest_scenic_score = current_score

print(highest_scenic_score)
