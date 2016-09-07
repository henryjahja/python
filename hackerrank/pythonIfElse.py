'''by shashank21j
Given an integer, , perform the following conditional actions:

If  is odd, print Weird
If  is even and in the inclusive range of  to , print Not Weird
If  is even and in the inclusive range of  to , print Weird
If  is even and greater than , print Not Weird
'''

#!/bin/python3

import sys


N = int(input().strip())
if N%2:
    print("Weird")
elif N>=2 and N<=5:
    print("Not Weird")
elif N>=6 and N<=20:
    print("Weird")
elif N>5:
    print("Not Weird")
    
