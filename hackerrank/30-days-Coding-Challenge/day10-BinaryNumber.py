''' by AvimanyuSingh
Given a base-10 integer, n, convert it to binary (base-2). Then find and print the base-10 integer denoting the maximum number of consecutive 1's in n's binary representation.
'''

import sys

#print(len(max(bin(int(input().strip()))[2:].split('0'))))

print(
    len(
        max(
            bin(
                int(
                    input().strip()
                )
            )[2:].split('0'))
        )
)
