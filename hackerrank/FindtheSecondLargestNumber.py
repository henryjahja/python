''' by harsh_beria93
You are given N numbers. Store them in a list and find the second largest number.
'''

N = int(input())
print(list(sorted(set(str(input()).split (" "))))[-2])
