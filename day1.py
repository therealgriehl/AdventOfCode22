### Advent of Code ###
    ### Day 1 ###

import numpy as np

# Part One and Two

data = np.loadtxt(r'C:\Users\rgrie\PycharmProjects\AdventOfCode22\input\1_1.txt')

with open(r'C:\Users\rgrie\PycharmProjects\AdventOfCode22\input\1_1.txt') as file_in:
    lines = []
    for line in file_in:
        if line == '\n':
            lines.append('X')
        else: lines.append(int(line))

counter = 0
calories = []
for item in lines:
    if item == 'X':
        calories.append(counter)
        counter = 0
    else: counter += item

calories.sort(reverse=True)
print(calories)
print(calories[0])
print(calories[1])
print(calories[2])
sum_cal = sum(calories[0:3])
print(sum_cal)
print(max(calories))
