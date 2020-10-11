#!/usr/bin/python3
import sys
a=[]
b=[]
for line in sys.stdin:
    a.append(line.strip().split(",")[0])
    b.append(line.strip().split(",")[1])
for i in range(len(a)):
     print(i,",",a[i])
for i in range(len(b)):
     print(i,",",b[i])
