#!/usr/bin/python3
import sys

from functools import reduce
d={}
dic={}
result1=0
for line in sys.stdin:
     key, value=line.strip().split(",")
     d.setdefault(key, []).append(int(value)) 
for i in d.values():
    result1 += reduce((lambda x, y: x * y), i)
    
print('final output', result1)
         


 
