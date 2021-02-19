# Using class-level and static methods


class Book:
    # Properties defined at the class level are shared by all instances
    BOOK_TYPES = ("HARDCOVER", "PAPERBACK", "EBOOK")
    # Double-underscore properties are hidden from other classes
    __booklist = None

    # static methods do not receive class or instance arguments and usually operate on data 
    # that is not instance- or class-specific.
    # They don't modify the state of either the class or a specific object instance
    @staticmethod
    def getbooklist():
        if Book.__booklist == None:
            Book.__booklist = []
        return Book.__booklist

    # class methods receive a class as their argument and can only operate on class-level data
    @classmethod
    def getbooktypes(cls):
        return cls.BOOK_TYPES

    # instance methods receive a specific object instance as an argument and operate on data 
    # specific to that object instance
    def setTitle(self, newtitle):
        self.title = newtitle

    def __init__(self, title, booktype):
        self.title = title
        if (not booktype in Book.BOOK_TYPES):
            raise ValueError(f"{booktype} is not a valid book type")
        else:
            self.booktype = booktype


# Access the class attribute
print("Book types: ", Book.getbooktypes())

# Create some book instances
b1 = Book("Title 1", "HARDCOVER")
# b2 = Book("Title 2", "COMIC")          # ValueError: COMIC is not a valid booktype
b2 = Book("Title 2", "PAPERBACK")

# Use the static method to access a singleton object
thebooks = Book.getbooklist()
thebooks.append(b1)
thebooks.append(b2)
print(thebooks)