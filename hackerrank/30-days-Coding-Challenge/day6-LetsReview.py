''' by allisonP
Given a string, S, of length N that is indexed from 0 to N-1, print its even-indexed and odd-indexed characters as 2 space-separated strings on a single line (see the Sample below for more detail).

Note: 0 is considered to be an even index.

'''

T=int(input())
S=[]
for x in range(0,T):
    S.append(str(input()))
for x in range(0,T):
    showCase=""
    for y in range(0,len(S[x])):
        tempString = S[x]
        if y == 0 or y% 2 == 0:
            showCase += tempString[y]
    showCase+=" "
    for y in range(0,len(S[x])):
        tempString = S[x]
        if y==1 or y % 2 == 1:
            showCase += tempString[y]
    print(showCase)
