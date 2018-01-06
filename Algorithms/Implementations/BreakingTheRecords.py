#!/bin/python

import sys

def breakingRecords(score):
    currentMaxScore = score[0]
    currentMinScore = score[0]
    maxCount = 0
    minCount = 0

    for i in score:
        if i > currentMaxScore:
            currentMaxScore = i
            maxCount += 1
        if i < currentMinScore:
            currentMinScore = i
            minCount += 1
    return [maxCount, minCount]




if __name__ == "__main__":
    n = int(raw_input().strip())
    score = map(int, raw_input().strip().split(' '))
    result = breakingRecords(score)
    print " ".join(map(str, result))


