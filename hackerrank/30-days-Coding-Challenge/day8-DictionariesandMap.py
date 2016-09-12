T= int(input())
tel={}
for x in range(0,T):
    inputTel = str(input()).split(" ")
    tel[inputTel[0]] = inputTel[1]
findTel = []
for x in range(0,T):
    findTel.append(str(input()))
for x in findTel:
    printThis=""
    if x in tel.keys():
        printThis+=x
        printThis+="="
        printThis+=tel[x]
        print(printThis)
    else:
        print("Not found")
