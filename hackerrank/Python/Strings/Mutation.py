''' by shashank21j
Read a given string, change the character at a given index and then print the modified string.
'''

a,b = list(input()), input().split(" ")
a[int(b[0])] = b[1]
print("".join(a))
