class Book:
    def __init__(self, title, isbn):
        self.__title=title
        self.isbn=isbn
    def __repr__(self):
        return "ISBN:"+ self.isbn+ ";TITLE:"+ self.__title
    
book=Book("The Python Tutorial", "0123456")
print(book)