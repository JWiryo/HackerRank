# -*- coding: utf-8 -*-

# Enter your code here. Read input from STDIN. Print output to STDOUT
import math

AB = float(raw_input())
BC = float(raw_input())

deg = int(round(math.atan2(AB, BC) * 180 / math.pi))

print str(deg) + "°"
