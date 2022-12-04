### Advent of Code ###
    ### Day 3 ###

# Part One

with open(r'C:\Users\rgrie\PycharmProjects\AdventOfCode22\input\3_1.txt') as file_in:
    content = []
    for line in file_in:
        line2 = line.rstrip()
        a = line2[(len(line2)//2):]
        b = line2[:(len(line2)//2)]
        content.append(a)
        content.append(b)

print(len(content))
print(content)
doubles = []
amount = 1
for i in range(0,len(content), 2):
    for letter in content[i]:
        if letter in content[i+1]:
            doubles.append(letter)
            break

print(len(doubles))
print(doubles)

scores = {}
point = 1
for c in list(map(chr,range(ord('a'),ord('z')+1))):
    scores[c] = point
    point += 1
points = 27
for c in list(map(chr,range(ord('A'),ord('Z')+1))):
    scores[c] = points
    points += 1
print(scores)

sum = 0

for element in doubles:
    sum = sum + scores[element]

print(sum)

# Part Two

with open(r'C:\Users\rgrie\PycharmProjects\AdventOfCode22\input\3_1.txt') as file_in:
    contenttwo = []
    for line in file_in:
        line2 = line.rstrip()
        contenttwo.append(line2)


triple = []
for i in range(0, len(contenttwo), 3):
    for let in contenttwo[i]:
        if let in contenttwo[i+1] and let in contenttwo[i+2]:
            triple.append(let)
            break
print(contenttwo)
print(len(triple))

sum_trip = 0
for element in triple:
    sum_trip = sum_trip + scores[element]

print(sum_trip)