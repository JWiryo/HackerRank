import math

scoreList = []

for _ in range(int(raw_input())):
    name = raw_input()
    score = float(raw_input())
    scoreList.append([name, score])

minScore = min(scoreList,  key=lambda x:x[1])[1]
secondLowest = max(scoreList, key=lambda x:x[1])[1]
secondLowestNameList = []

for scoring in scoreList:
    if minScore < scoring[1] <= secondLowest:
        secondLowest = scoring[1]

for list in scoreList:
    if list[1] == secondLowest:
        secondLowestNameList.append(list[0])

for name in sorted(secondLowestNameList):
    print name
