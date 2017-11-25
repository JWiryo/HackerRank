#!/bin/python

import sys

def timeConversion(s):
    # Complete this function
    hour = int(s[0:2]);
    newTime = "";

    if 'P' in s[-2]:
        hour += 12;
        newTime = str(hour)+s[2:8];
        if(hour == 24):
            newTime = '12'+s[2:8];
        return newTime;
    else:
        newTime = s[0:8]
        if(hour == 12):
            newTime = '00'+s[2:8];
        return newTime;

s = raw_input().strip()
result = timeConversion(s)
print(result)
