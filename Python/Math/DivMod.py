from __future__ import print_function;

# Enter your code here. Read input from STDIN. Print output to STDOUT
a = int(raw_input())
b = int(raw_input())

print("{}\n{}\n{}".format(a // b, a % b, divmod(a, b)))
