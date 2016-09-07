'''by darkshadows
John Watson performs an operation called a right circular rotation on an array of integers, [a0,a1,...an-1]. After performing one right circular rotation operation, the array is transformed from [a0,a1,...an-1] to [an-1,a0,a1,...an-2].

Watson performs this operation k times. To test Sherlock's ability to identify the current element at a particular position in the rotated array, Watson asks q queries, where each query consists of a single integer, m, for which you must print the element at index  in the rotated array (i.e., the value of am).
'''

nkq = input().split(" ")
n = int(nkq[0])
k = int(nkq[1])
q = int(nkq[2])
a = list(input().split(" "))
m=[]
for x in range(0,q):
    m.append(int(input()))
for x in range(0,k):
    a.insert(0, a.pop())
for x in m:
    print (a[x])
