''' by shashank21j
Read an integer N.
Without using any string methods, try to print the following:
123...N
Note that "..." represents the values in between.
'''

i=int(input())
o=""
for x in range(0,i):
    o+=str(x+1)
print(o)
