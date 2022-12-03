

with open(r'C:\Users\rgrie\PycharmProjects\AdventOfCode22\input\2_1.txt') as file_in:
    guide = []
    for line in file_in:
        line2 = line.rstrip()
        b = line2.split(' ')
        guide.append(b)

print(guide)

'''
A = Rock / B = Paper / C = Scissors
X = Rock 1 / Y = Paper 2 / Z = Scissors 3
W = 6 / D = 3 / L = 0

X = L / Y = D / Z = W
'''
scoring = [
    ['A', 'X'],[4], ['A', 'Y'],[8], ['A', 'Z'],[3],
    ['B', 'X'],[1],['B', 'Y'],[5],['B', 'Z'],[9],
    ['C', 'X'],[7],['C', 'Y'],[2],['C', 'Z'],  [6],
]
score = 0

for i in range(len(guide)):
    for j in range(0, 18, 2):
        if guide[i] == scoring[j]:
            val = sum(scoring[j+1])
            score += val

print(score)

scoring2 = [
    ['A', 'X'],[3], ['A', 'Y'],[4], ['A', 'Z'],[8],
    ['B', 'X'],[1],['B', 'Y'],[5],['B', 'Z'],[9],
    ['C', 'X'],[2],['C', 'Y'],[6],['C', 'Z'],  [7],
]
score2 = 0

for i in range(len(guide)):
    for j in range(0, 18, 2):
        if guide[i] == scoring2[j]:
            val2 = sum(scoring2[j+1])
            score2 += val2

print(score2)