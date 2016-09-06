'''by aa1992
In this challenge, we're getting started with conditional statements. Check out the Tutorial tab for learning materials and an instructional video!

Task
Given an integer, n, perform the following conditional actions:

If n is odd, print 'Weird'
If n is even and in the inclusive range of 2 to 5, print 'Not Weird'
If n is even and in the inclusive range of 6 to 20, print 'Weird'
If n is even and greater than 20, print 'Not Weird'
Complete the stub code provided in your editor to print whether or not n is weird.
'''

#!/bin/python3

import sys


N = int(input().strip())
if N % 2 == 1:
    print("Weird")
elif N >= 2 and N <= 5:
    print("Not Weird")
elif N >= 7 and N <= 20:
    print("Weird")
else:
    print("Not Weird")
