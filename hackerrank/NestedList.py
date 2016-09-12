''' by harsh_beria93
Given the names and grades for each student in a Physics class of N students, store them in a nested list and print the name(s) of any student(s) having the second lowest grade.

Note: If there are multiple students with the same grade, order their names alphabetically and print each name on a new line.
'''

from operator import itemgetter
N = int(input())
g = []
for x in range(0,N):
    p = str(input())
    l = float(input())
    g.append([p,l])
g.sort(key=itemgetter(1))
h = []
for x in g:
    h.append(x[1])
h = list(sorted(set(h)))[1]
namel = []
for x in g:
    if x[1] == h:
        namel.append(x[0])
namel = sorted(namel)
names = ""
for x in namel:
    names+= str(x)
    names+= "\n"
print(names[:-1])









#shortest
n = int(input())
marksheet = [[input(), float(input())] for _ in range(n)]
second_highest = sorted(list(set([marks for name, marks in marksheet])))[1]
print('\n'.join([a for a,b in sorted(marksheet) if b == second_highest]))
