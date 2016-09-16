''' by DOSHI
You are given a string S. 
Your task is to find out if the string S contains: alphanumeric characters, alphabetical characters, digits, lowercase and uppercase characters.
'''

str = input()
print (any(c.isalnum()  for c in str))
print (any(c.isalpha() for c in str))
print (any(c.isdigit() for c in str))
print (any(c.islower() for c in str))
print (any(c.isupper() for c in str))
