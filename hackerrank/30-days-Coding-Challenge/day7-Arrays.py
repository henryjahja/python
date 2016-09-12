''' by saikiran9194
Given an array, A, of N integers, print A's elements in reverse order as a single line of space-separated numbers.
'''

#!/bin/python3

import sys


n = int(input().strip())
arr = [int(arr_temp) for arr_temp in input().strip().split(' ')]
for x in range(0,len(arr)):
    print(arr[len(arr)-1-x], end=" ")
