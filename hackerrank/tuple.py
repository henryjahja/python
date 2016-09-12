''' by shashank21j
Given an integer, n, and n space-separated integers as input, create a tuple, t, of those n integers. Then compute and print the result of hash(t).
'''
n = int(input())
t = tuple(int(x.strip()) for x in input().split(' '))
print (hash(t))
