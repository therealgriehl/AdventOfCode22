### Advent of Code ###
### Day 6 ###

# Part One -> set index in contents to 4
# Part Two -> set index in contents to 14

with open(r'input/6_1.txt') as file_in:
    contents = file_in.read()

for i in range(len(contents)):
    if len(contents[0 + i:14 + i]) == len(set(contents[0 + i:14 + i])):
        print(i + 14)
        break
