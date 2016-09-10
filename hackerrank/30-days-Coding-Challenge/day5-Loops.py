''' by AvimanyuSingh
Given an integer, N, print its first 10 multiples. Each multiple N x i (where 1 <= i <= 10) should be printed on a new line in the form: N x i = result.

'''

#!/bin/python3

import sys


N = int(input().strip())
for x in range(1,11):
    print(N,"x",x,"=",N*x)
