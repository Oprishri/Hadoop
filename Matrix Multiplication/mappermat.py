#!/usr/bin/python3
import sys
for line in sys.stdin:
	matrix_index, row, col, value = line.rstrip().split(",")
	if matrix_index == 'A':
	   for i in range(2):
               key = row + "," + str(i)
               print(key,col,value)
	else:
           for j in range(2):
               key = str(j) + "," + col 
               print(key,row,value)


