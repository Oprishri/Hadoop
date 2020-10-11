#!/usr/bin/python3
import sys
data1={}
data2={}
result={}
for line in sys.stdin:
   l=line.strip().split(',')
   if(len(l)==1):
      continue
   elif(len(l)==2):
      data1[l[0]]=l[1]
   else:
      data2[l[0],l[1]]=l[2]
print("Data1 : \n",data1,"\n","Data2 : \n",data2)
print("For joint data1 join data2 ")
for i in data1.keys():
     k=0
     for j in data2.keys():
        if(i==j[1]):
           k=1
           break
     if(k==1):
       result[i,j[0]]=data1[i]+" "+data2[j]
for i in result.keys():
    print(i," ",result[i])
     
           
