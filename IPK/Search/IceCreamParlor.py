#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the whatFlavors function below.
# This is the Two-Sum Algorithm Solution to this problem
def whatFlavors(cost, money):
    costDict = {}

    for d in range(len(cost)):
        complement = money - cost[d]
        if complement in costDict:
            print(costDict[complement] + 1, d + 1)
        costDict[cost[d]] = d


if __name__ == '__main__':
    t = int(input())

    for t_itr in range(t):
        money = int(input())

        n = int(input())

        cost = list(map(int, input().rstrip().split()))

        whatFlavors(cost, money)
