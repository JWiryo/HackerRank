# Enter your code here. Read input from STDIN. Print output to STDOUT
import math
import cmath

complexInput = str(raw_input());
complexNumber = complex(complexInput);
x = complexNumber.real
y = complexNumber.imag

r = math.sqrt(x**2 + y**2)
theta = cmath.phase(complexNumber)
print "{}\n{}".format(r, theta)