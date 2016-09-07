'''by shashank21j
Given an array of N integers, can you find the sum of its elements?
'''

#!/bin/python3

import sys


n = int(input().strip())
arr = [int(arr_temp) for arr_temp in input().strip().split(' ')]
tot = 0
for x in arr:
    tot += x
print (tot)

