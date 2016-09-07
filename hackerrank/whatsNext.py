'''by forthright48
Johnny is playing with a large binary number, B. The number is so large that it needs to be compressed into an array of integers, A, where the values in even indices (0, 2, 4, ...) represent some number of consecutive 1 bits and the values in odd indices (1, 3, 5, ...) represent some number of consecutive 0 bits in alternating substrings of B.

For example, suppose we have array A = {4, 1, 3, 2, 4}. A0 represents "1111", A1 represents "0", A2 represents "111", A3 represents "00", and A4 represents "1111". The number of consecutive binary characters in the i-th substring of B corresponds to integer Ai, as shown in this diagram:
		4|1|3|2|4
	1111|0|111|00|1111

When we assemble the sequential alternating sequences of 1's and 0's, we get B = "11110111001111".

We define setCount(B) to be the number of 1's in a binary number, B. Johnny wants to find a binary number, D, that is the smallest binary number >B where setCount(B) = setCount(D). He then wants to compress D into an array of integers, C (in the same way that integer array A contains the compressed form of binary string B).

Johnny isn't sure how to solve the problem. Given array A, find integer array C and print its length on a new line. Then print the elements of array  as a single line of space-separated integers.
'''

T = int(input())
while T > 0:
    T -= 1
    An = int(input())
    A = str(input()).split(" ")
    A = [ int(x) for x in A ]
    if An == 1:
        if A[0] == 1:
            C = [A[0],1]
        else:
            C = [1,1,A[0]-1]
    elif An == 2:
        C = [1,A[1]+1,A[0]-1]
        if C[len(C)-1] == 0:
            del C[-1]
    elif An % 2 == 1:
        C = A
        C.append(1)
        C.append(C[len(C)-2]-1)
        C[len(C)-3] = 1
        C[len(C)-4] -= 1
        
    else:
        C = A
        C.append(0)
        C[len(C)-1] = C[len(C)-3]-1
        C[len(C)-2] += 1
        C[len(C)-3] = 1
        C[len(C)-4] -= 1
        
    if C[len(C)-1] == 0:
        del C[-1]        
    posThis = -1
    for x in C:
        posThis += 1
        if x == 0:
            del C[posThis]
            del C[posThis]
            C[posThis-1] += 1
    print (len(C))
    printC = ""
    for x in C:
        printC += str(x)
        printC += " "
    printC = printC[:-1]
    print (printC)
