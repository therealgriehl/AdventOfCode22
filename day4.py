### Advent of Code ###
    ### Day 4 ###

# Part One

with open(r'C:\Users\rgrie\PycharmProjects\AdventOfCode22\input\4_1.txt') as file_in:
    sections = []
    for line in file_in:
        line = line.rstrip()
        a, c = line.split(',')
        a, b = a.split('-')
        c, d = c.split('-')
        sections.append([int(a),int(b), int(c), int(d)])

print(len(sections))
print(sections)

pairs = 0
for i in range(len(sections)):
    if sections[i][0] >= sections[i][2] and sections[i][1] <= sections[i][3]:
        pairs += 1
    elif sections[i][2] >= sections[i][0] and sections[i][3] <= sections[i][1]:
        pairs += 1

print(pairs)

# Part Two

ranges = 0

for j in range(len(sections)):
    if sections[j][2] <= sections[j][0] <= sections[j][3]:
        ranges += 1
        continue
    elif sections[j][2] <= sections[j][1] <= sections[j][3]:
        ranges += 1
        continue
    elif sections[j][0] < sections[j][2] and sections[j][1] > sections[j][3]:
        ranges += 1
        continue

print(ranges)

