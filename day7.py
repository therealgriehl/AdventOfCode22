### Advent of Code ###
### Day 6 ###

import re

# Part One
structure = {}

with open(r'input/7_1.txt') as file_in:
    current_dir = ''

    for line in file_in:
        line = line.rstrip()
        if line.startswith('$ cd ..'):
            current_dir = current_dir[0:(len(current_dir)-len(copy_dir)-1)]

            continue

        if line.startswith('$ cd'):
            line = line.split(' ')
            copy_dir = line[2]
            if current_dir + '/' + line[2] in structure:
                continue
            current_dir = current_dir + '/' + line[2]
            structure[current_dir] = 0

        elif line[:1].isdigit():
            count = structure[current_dir] + int(re.search(r'\d+', line).group())
            structure[current_dir] = count

dir_sizes = list(structure.values())
print(dir_sizes)
print(sum(item for item in dir_sizes if item < 100000))



