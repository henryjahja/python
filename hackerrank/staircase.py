'''by vatsalchanana
Consider a staircase of size n=4:

   #
  ##
 ###
####

Observe that its base and height are both equal to n, and the image is drawn using # symbols and spaces. The last line is not preceded by any spaces.

Write a program that prints a staircase of size n.
'''

#!/bin/python3

import sys


n = int(input().strip())
staircase = ""
for x in range(0,n):
    for y in range(0,n-x-1):
        staircase+= " "
    for z in range(0,x+1):
        staircase+= "#"
    if x!=n-1:
        staircase+="\n"
staircase[:-2]
print (staircase)
