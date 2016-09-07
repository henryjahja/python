'''by dheeraj
The Utopian Tree goes through 2 cycles of growth every year. Each spring, it doubles in height. Each summer, its height increases by 1 meter.

Laura plants a Utopian Tree sapling with a height of 1 meter at the onset of spring. How tall will her tree be after growth cycles?
'''

#!/bin/python3

import sys


t = int(input().strip())
N=[]
for a0 in range(t):
    n = int(input().strip())
    N.append(n)
H=[]
counter=0
for x in range(t):
    H.append(0)
    for y in range(0,N[counter]+1):
        if y==0:
            H[counter]+=1
        elif y % 2 == 0:
            H[counter]+=1
        elif y % 2 == 1:
            H[counter]*=2
    counter+=1
for x in H:
    print(x)
    
    
    
    
    
    
    
