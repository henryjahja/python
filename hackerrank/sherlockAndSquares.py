'''by darkshadows
Watson gives two integers (A and B) to Sherlock and asks if he can count the number of square integers between A and B (both inclusive).
Note: A square integer is an integer which is the square of any integer. For example, 1, 4, 9, and 16 are some of the square integers as they are squares of 1, 2, 3, and 4, respectively.
'''
import math
T=int(input(""))
TC = []
count = 0
while T>0:
    AB = str(input()).split(" ")
    A = int(AB[0])
    B = int(AB[1])
    TC.append(int(math.floor(math.sqrt(B))-math.ceil(math.sqrt(A))+1))
    count+=1
    T-=1
for x in TC:
    print (x)
