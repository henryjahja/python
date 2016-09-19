''' by Shafaet
Given a Book class and a Solution class, write a MyBook class that does the following:

Inherits from Book
Has a parameterized constructor taking these 3 parameters:
1. string title
2. string author
3. int price
Implements the Book class' abstract display() method so it prints these 3 lines:
1. Title:, a space, and then the current instance's title.
2. Author:, a space, and then the current instance's author.
3. Price:, a space, and then the current instance's price.
Note: Because these classes are being written in the same file, you must not use an access modifier (e.g.: public) when declaring MyBook or your code will not execute.
'''

#locked ↓
from abc import ABCMeta, abstractmethod
class Book(object, metaclass=ABCMeta):
    def __init__(self,title,author):
        self.title=title
        self.author=author   
    @abstractmethod
    def display(): pass
#locked ↑
#Write MyBook class
class MyBook(Book):
    def __init__(self, title, author, price):
        super(Book, self).__init__()
        self.price = price 
    def display(self):
        print("Title: %s\nAuthor: %s\nPrice: %d" % (title, author, price))
#locked ↓
title=input()
author=input()
price=int(input())
new_novel=MyBook(title,author,price)
new_novel.display()
#locked ↑
