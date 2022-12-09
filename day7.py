### Advent of Code ###
### Day 6 ###

import re
from collections import defaultdict

# Part One

path = []
all_paths = [] # only for check if entering same file multiple times possible
sizes = defaultdict(int)

with open(r'AdventOfCode22\input\7_1.txt') as file_in:
    

    for line in file_in:
        line = line.rstrip()
        start = line.split()[0]
        end = line.split()[-1]

        if line.startswith('$ cd'):
            
            if end == '..':
                path.pop()
                print('Moving up')
                continue

            elif end == '/':
                path.append('root')
                print('You are at Root')

            else:
                path.append(end)
                print(f'New path is {path}')

        elif line.startswith('$ ls'):
            print('Listing directory')

        elif start == 'dir':
            print(f'Directory named: {end}')

        elif re.match('^\d+', line):
            filesize = line.split()[0]
            
            for i in range(len(path)):
                sizes['/'.join(path[:i+1])] += int(filesize)



dir_sizes = list(sizes.values())
print(dir_sizes)
print(sum(item for item in dir_sizes if item < 100000))

# Part Two
space_used = sizes['root']
print(f'Total used space is {space_used}')
space_needed = 30000000 - (70000000 - space_used)
print(f'Space needed is {space_needed}')

deletable_dirs = [dir for dir in sizes.values() if  dir >= space_needed]

print(f'Smallest directory to delete is {min(deletable_dirs)} in size')



