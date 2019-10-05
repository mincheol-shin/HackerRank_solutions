from abc import ABCMeta, abstractmethod

# Abstract Class
class Book(object, metaclass=ABCMeta):

    def __init__(self,title,author):
        self.title=title
        self.author=author

    @abstractmethod
    def display(self):
        pass

class MyBook(Book):

    __slots__ = ["price"]

    def __init__(self,title, author, price):
        super().__init__(title, author)
        self.price = price

    def display(self):
        print("Title: {}".format(title))
        print("Author: {}".format(author))
        print("Price: {}".format(price))


title=input()
author=input()
price=int(input())
new_novel=MyBook(title,author,price)
new_novel.display()