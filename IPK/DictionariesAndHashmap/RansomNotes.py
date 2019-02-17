#!/bin/python3

import math
import os
import random
import re
import sys

from collections import Counter


# Complete the checkMagazine function below.
def checkMagazine(magazine, note):
    mCounter = Counter(magazine)
    nCounter = Counter(note)

    if (nCounter - mCounter == {}):
        print("Yes")
    else:
        print("No")

    # m_dict = {}
    # n_dict = {}
    # result_dict = {}

    # for i in range(len(magazine)):
    #     m_dict[i] = magazine[i]

    # for j in range(len(note)):
    #     n_dict[j] = note[j]

    # for n_key, n_value in list(n_dict.items()):
    #     for m_key, m_value in list(m_dict.items()):
    #         if m_value == n_value:
    #             result_dict[n_key] = n_value
    #             del(m_dict[m_key])

    # if len(n_dict) == len(result_dict):
    #     print("Yes")
    # else:
    #     print("No")


if __name__ == '__main__':
    mn = input().split()

    m = int(mn[0])

    n = int(mn[1])

    magazine = input().rstrip().split()

    note = input().rstrip().split()

    checkMagazine(magazine, note)
