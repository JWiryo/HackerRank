#!/bin/python

import sys


s,t = raw_input().strip().split(' ')
s,t = [int(s),int(t)]
a,b = raw_input().strip().split(' ')
a,b = [int(a),int(b)]
m,n = raw_input().strip().split(' ')
m,n = [int(m),int(n)]
apple = map(int,raw_input().strip().split(' '))
orange = map(int,raw_input().strip().split(' '))


def countAppleAndOrange():
    global appleInCount, orangeInCount
    appleInCount = orangeInCount = 0;
    countApple()
    countOrange()


def countOrange():
    global orangeInCount
    for eachOrange in orange:
        if s <= b + eachOrange <= t:
            orangeInCount += 1;
        else:
            pass


def countApple():
    global appleInCount
    for eachApple in apple:
        if s <= a + eachApple <= t:
            appleInCount += 1;
        else:
            pass


countAppleAndOrange()

print appleInCount;
print orangeInCount;