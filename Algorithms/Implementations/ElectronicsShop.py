#!/bin/python

import sys

def getMoneySpent(keyboards, drives, s):
    maxPriceList = []
    for keyboard in keyboards:
        for drive in drives:
            if(keyboard + drive <= s):
                maxPriceList.append(keyboard+drive)
    if maxPriceList:
        return max(maxPriceList)
    else:
        return -1


s,n,m = raw_input().strip().split(' ')
s,n,m = [int(s),int(n),int(m)]
keyboards = map(int, raw_input().strip().split(' '))
drives = map(int, raw_input().strip().split(' '))
#  The maximum amount of money she can spend on a keyboard and USB drive, or -1 if she can't purchase both items
moneySpent = getMoneySpent(keyboards, drives, s)
print(moneySpent)
