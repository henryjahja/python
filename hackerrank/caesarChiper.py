'''by vatsalchanana
Julius Caesar protected his confidential information by encrypting it in a cipher. Caesar's cipher rotated every letter in a string by a fixed number, K, making it unreadable by his enemies. Given a string, S, and a number, K, encrypt S and print the resulting string.

Note: The cipher only encrypts letters; symbols, such as -, remain unencrypted.
'''

#!/bin/python3

import sys
import re
n = 0
while n <1 or n >100:
    n = int(input("").strip())
while True:
    s = input("").strip()
    if len(s) == n:
        break
k = -1
while k <0 or k >100:
    k = int(input("").strip()) % 26
eW = ""
teW=""
for x in s:
    regexAll = r"([a-zA-Z])"
    regexLow = r"([a-z])"
    regexHi = r"([A-Z])"
    if re.search(regexHi, x) and ord(x)+k > 90:
        eW+=chr(ord(x) + k - 26)
    elif re.search(regexLow, x) and ord(x)+k > 122:
        eW+=chr(ord(x) + k - 26)
    elif re.search(regexAll, x):
        eW+=chr(ord(x) + k)
    else:
        eW+=x
print (eW)
