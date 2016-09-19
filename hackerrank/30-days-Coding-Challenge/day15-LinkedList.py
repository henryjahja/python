''' by harsha_s
Complete the insert function in your editor so that it creates a new Node (pass data as the Node constructor argument) and inserts it at the tail of the linked list referenced by the head parameter. Once the new node is added, return the reference to the head node.

Note: If the head argument passed to the insert function is null, then the initial list is empty.
'''

#locked ↓
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None 
class Solution: 
    def display(self,head):
        current = head
        while current:
            print(current.data,end=' ')
            current = current.next

mylist= Solution()
T=int(input())
head=None
for i in range(T):
    data=int(input())#locked ↑
    def insert(self,head,data): 
    #Complete this method
        print (data, end = " ")
#locked ↓
    head=mylist.insert(head,data)    
mylist.display(head); 
#locked ↑
