#variable switching
fiboInput = 0
while int(fiboInput) <= 0:
	fiboInput = int(input("Input Fibonacci iteration you would like: "))
counter = 0
curNum = 0
prevNum = 0
newNum = 0
while counter < fiboInput:
	counter +=1
	if counter == 1 or counter == 2:
		newNum = 1
	elif counter >= 3:
		newNum = curNum + prevNum
	prevNum = curNum
	curNum = newNum
	newNum = "{:,}".format(newNum)
	print ("Iteration #%d: %s" % (counter,newNum))
	
#recursion
def fibo(x):
    if x == 0:
        return 0
    elif x == 1:
        return 1
    else:
        return fibo(x-1) + fibo(x-2)
for x in range(200):
	print(x,fibo(x))
