#!/bin/python

import sys

def solve(year):
    if year == 1918:
        return"26.09.{}".format(year)
    elif isLeap(year):
        return "12.09.{}".format(year)
    else:
        return "13.09.{}".format(year)


def isLeap(year):
    if year < 1917 and year % 4 == 0:
        return True
    elif year % 4 ==0 and (year % 400 == 0 or (year % 4 == 0 and year % 100 != 0)):
        return True
    else:
        return False


year = int(raw_input().strip())
result = solve(year)
print(result)
