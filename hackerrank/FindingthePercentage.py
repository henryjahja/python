''' by harsh_beria93
You have a record of N students. Each record contains the student's name, and their percent marks in Maths, Physics and Chemistry. The marks can be floating values. The user enters some integer N followed by the names and marks for N students. You are required to save the record in a dictionary data type. The user then enters a student's name. Output the average percentage marks obtained by that student, correct to two decimal places.
'''

n = int(input())
marksheet = []
for _ in range(n):
    al = str(input()).split(" ")
    marksheet.append([al[0],((float(al[1])+float(al[2])+float(al[3]))/3)])
na=input()
for z in marksheet:
    if z[0] ==na:
        print ("%.2f" % z[1])
        break
