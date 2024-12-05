# Problem Statement: You are maintaining a library system where each book is 
# stored as a tuple within a list. Your task is to update this system by 
# adding new books and ensuring no duplicates.

# Existing Library Data: 
# 
library = [("1984", "George Orwell"), ("Brave New World", "Aldous Huxley")] 

# Add functionality to insert new books into `library`. 
# Ensure that adding a duplicate book is handled appropriately.


def add_book(library, new_book):
    if new_book in library:
        print(f"The book '{new_book[0]}' by {new_book[1]} is already in the library. ")
    else:
        library.append(new_book)
        print(f"The book '{new_book[0]}' by {new_book[1]}' has been addedto the library. ")
    return library

# Example Usage 

new_book1 = ("1984", "George Orwell") 
new_book2 = ("Fahrenheit 451", "Ray Bradbury") 

library = add_book(library, new_book1) 
library = add_book(library, new_book2) 

print(library)