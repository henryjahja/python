'''by kevinsogo
You are the benevolent ruler of Rankhacker Castle, and today you're distributing bread to a straight line of N subjects. Each i-th subject (where 1<= i <= N) already has Bi loaves of bread.

Times are hard and your castle's food stocks are dwindling, so you must distribute as few loaves as possible according to the following rules:

Every time you give a loaf of bread to some person i, you must also give a loaf of bread to the person immediately in front of or behind them in the line (i.e., persons i+1 or i-1).
After all the bread is distributed, each person must have an even number of loaves.
Given the number of loaves already held by each citizen, find and print the minimum number of loaves you must distribute to satisfy the two rules above. If this is not possible, print NO.
'''


#!/bin/python3

import sys

N = int(input().strip())
B = [int(B_temp) for B_temp in input().strip().split(' ')]
evenSum = 0
for x in B:
    evenSum+= x
if evenSum %2 == 1:
    print("NO")
else:
    breadLoafes=0
    shouldShare = 1
    while shouldShare == 1:
        shouldShare = 0
        for x in range(0,(len(B))):
            if B[x]%2==1:
                if x == (len(B)-1):
                    B[x]+=1
                    B[x-1]+=1
                    breadLoafes+=2
                elif x == 0:
                    B[x]+=1
                    B[x+1]+=1
                    breadLoafes+=2
                else:
                    B[x]+=1
                    B[x+1]+=1
                    breadLoafes+=2

        for x in range(0,(len(B))):
            if B[x]%2==1:
                shouldShare=1
                break
    #print(B)
    print(breadLoafes)
