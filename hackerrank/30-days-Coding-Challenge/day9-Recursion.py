''' by AvimanyuSingh
Write a factorial function that takes a positive integer, N as a parameter and prints the result of N! (N factorial).
Note: If you fail to use recursion or fail to name your recursive function factorial or Factorial, you will get a score of .
'''

def factorial(c):
    if c!=1:
        return c*factorial(c-1)
    else:
        return c*1
print(factorial(int(input())))
