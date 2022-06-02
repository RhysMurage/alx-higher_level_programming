#!/usr/bin/python3
from sys import argv

n = len(argv)
argSum = 0
for i in range(1, n):
    argSum += int(argv[i])
print(argSum)
