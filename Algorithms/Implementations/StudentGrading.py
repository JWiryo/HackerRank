#!/bin/python

import sys
import math

def solve(grades):
    # Complete this function
    newScores = []
    for score in grades:
        if score < 38:
            newScores.append(score);
        elif (roundToNearest5(score) - score) < 3:
            newScores.append(roundToNearest5(score));
        else:
            newScores.append(score);
    return newScores;



def roundToNearest5(scoreToRound):
    return int(5 * math.ceil((float(scoreToRound))/5));

n = int(raw_input().strip())
grades = []
grades_i = 0
for grades_i in xrange(n):
    grades_t = int(raw_input().strip())
    grades.append(grades_t)
result = solve(grades)
print "\n".join(map(str, result))


