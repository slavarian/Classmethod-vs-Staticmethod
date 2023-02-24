class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def __eq__(self, other):
        if isinstance(other, Book):
            return self.title == other.title and self.author == other.author
        return False
    
book1 = Book("A", "B")
book2 = Book("A", "B")
book3 = Book("A", "C")

print(book1 == book2) 
print(book1 == book3) 