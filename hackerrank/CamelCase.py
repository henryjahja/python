''' by nabila_ahmed
Alice wrote a sequence of words in CamelCase as a string of letters, s, having the following properties:

It is a concatenation of one or more words consisting of English letters.
All letters in the first word are lowercase.
For each of the subsequent words, the first letter is uppercase and rest of the letters are lowercase.
Given s, print the number of words in s on a new line.

'''

#!/bin/python3

import sys
import re

print(len(re.sub('[a-z]', '', input()))+1)

#other
print(sum(map(str.isupper, input())) + 1)
