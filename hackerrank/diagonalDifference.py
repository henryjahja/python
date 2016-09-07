'''by vatsalchanana
Given a square matrix of size NxN, calculate the absolute difference between the sums of its diagonals.
'''

#!/bin/python3

import sys


n = int(input().strip())
a = []
for a_i in range(n):
    a_t = [int(a_temp) for a_temp in input().strip().split(' ')]
    a.append(a_t)
primaryDiagonal = 0
secondaryDiagonal = 0
y = 0
for x in a:
    #print(x[y])
    primaryDiagonal += x[y]
    #print(x[n-y-1])
    secondaryDiagonal += x[n-y-1]
    y+=1
print (abs(primaryDiagonal-secondaryDiagonal))
