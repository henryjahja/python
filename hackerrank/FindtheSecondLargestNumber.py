''' by harsh_beria93
You are given N numbers. Store them in a list and find the second largest number.
'''

N = int(input())
n = str(input()).split (" ")
print(list(sorted(set([int(x) for x in n])))[-2])
