'''by vatsalchanana
Given an array of integers, calculate which fraction of its elements are positive, which fraction of its elements are negative, and which fraction of its elements are zeroes, respectively. Print the decimal value of each fraction on a new line.

Note: This challenge introduces precision problems. The test cases are scaled to six decimal places, though answers with absolute error of up to 10^-4 are acceptable.
'''

#!/bin/python3

import sys


n = int(input().strip())
arr = [int(arr_temp) for arr_temp in input().strip().split(' ')]
pluses = 0
zeros = 0
negatives = 0
for x in arr:
    if x > 0:
        pluses+=1
    elif x == 0:
        zeros+=1
    elif x < 0:
        negatives+=1
print('%.6f' % (pluses/n))
print('%.6f' % (negatives/n))
print('%.6f' % (zeros/n))
