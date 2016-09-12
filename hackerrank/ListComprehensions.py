''' by harsh_beria93
You are given three integers X, Y and Z representing the dimensions of a cuboid. You have to print a list of all possible coordinates on a 3D grid where the sum of Xi + Yi + Zi is not equal to N. If X = 2, the possible values of Xi can be 0, 1 and 2. The same applies to Y and Z.
'''

x, y, z, n = (int(input()) for _ in range(4))
print ([[a,b,c] for a in range(0,x+1) for b in range(0,y+1) for c in range(0,z+1) if a + b + c != n ])
