'''
In this task, we would like for you to appreciate the usefulness of the groupby() function of itertools . To read more about this function, Check this out .

You are given a string S. Suppose a character 'c' occurs consecutively X times in the string. Replace these consecutive occurrences of the character 'C' with (X, c) in the string.
'''

from itertools import groupby
l = [list(g) for k, g in groupby(input())]
pr = ""
for x in l:
    pr+= "("
    pr+= str(len(x))
    pr+= ", "
    pr+= str(x[0])
    pr+= ") "
print(pr[:-1])
