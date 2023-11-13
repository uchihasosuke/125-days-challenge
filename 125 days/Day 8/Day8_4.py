 
#Write a program to create a Python class representing a book with attributes like title and author
 
class Book:
 
    def __init__(self, title, author):
 
        self.title = title
 
        self.author = author
 
 
# Creating an instance of a book
 
my_book = Book("The Great Gatsby", "F. Scott Fitzgerald")
 
 
# Accessing the attributes
 
print("Book title:", my_book.title)
 
print("Book author:", my_book.author)
 
