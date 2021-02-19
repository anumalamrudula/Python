# Basic class definitions


# Create a basic class
# () after a className is required only if we are going to indicate that the class inherits from another class.
class Book:
    # the "init" function is called when the instance is created and ready to be initialized
    def __init__(self, title):
        self.title = title


# Create instances of the class
book1 = Book("Brave New World")
book2 = Book("War and Peace")

# Print the class and property
print(book1)
print(book1.title)