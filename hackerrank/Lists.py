''' by shashank21j
Consider a list (list = []). You can perform the following commands:

insert i e: Insert integer e at position i.
print: Print the list.
remove e: Delete the first occurrence of integer e.
append e: Insert integer e at the end of the list.
sort: Sort the list.
pop: Pop the last element from the list.
reverse: Reverse the list.
Initialize your list and read in the value of n followed by n lines of commands where each command will be of the 7 types listed above. Iterate through each command in order and perform the corresponding operation on your list.
'''


def listInsert(n,i,e):
    i=int(i)
    n.insert( i, e)
    #n = [int(x) for x in n]
    return n
def listPrint(n):
    n = [int(x) for x in n]
    print(n)
    return n
def listRemove(n,e):
    if n:
        n.remove(int(e))
    return n
def listAppend(n,e):
    n.append(int(e))
    return n
def listSort(n):
    return sorted(n)
def listPop(n):
    if n:
        n.pop()
    return n
def listReverse(n):
    n.reverse()
    return n
    
l=[]
T=int(input())
for x in range(0,T):
    option = str(input()).split(" ")
    if option[0] == "insert":
        l = listInsert(l,option[1],option[2])
    elif option[0] == "print":
        l = listPrint(l)        
    elif option[0] == "remove":
        l = listRemove(l,option[1]) 
    elif option[0] == "append":
        l = listAppend(l,option[1]) 
    elif option[0] == "sort":
        l = listSort(l) 
    elif option[0] == "pop":
        l = listPop(l) 
    elif option[0] == "reverse":
        l = listReverse(l) 
