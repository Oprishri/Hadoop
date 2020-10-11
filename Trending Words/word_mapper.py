#!/usr/bin/python3
import sys
text=[]
date=[]
for line in sys.stdin:
     a=line.strip().split(',')
     text.append(a[0])
     date.append(a[1])
for i in range(len(text)):
    for j in text[i].split(' '):
      #if(len(j)!=0):
        print(j, date[i].split(' ')[0],",", 1)
