#!/usr/bin/python3
import sys
from functools import reduce
value1=[]
index1=[]
prod=[]
p=0
sum=0
for line in sys.stdin:
    cur_index,index,value= line.strip().split(" ")
    index1.append(int(index))
    value1.append(int(value))
i=0
while(i<16):
    if index1[i]==index1[i+1]:
        p=value1[i]*value1[i+1]
        prod.append(p)
        i+=2
print(prod)
for i in range(0,8,2):
    sum=prod[i]+prod[i+1]
    print(sum)
    sum=0
