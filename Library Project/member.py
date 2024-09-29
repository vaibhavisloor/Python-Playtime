from library import Book,Library

class Member:
    def __init__(self,name,phone):
        self.name = name
        self.phone = int(phone)
        self.book_borrowed = 0
        self.book_borrowed_list = []

    def borrow_book(self, book_nam, library):
        for book in library.book_list:
            if book.book_name == book_nam:
                self.book_borrowed_list.append(book_nam)
                library.book_list.remove(book)
                print(f"Book '{book.book_name}' by {book.book_author} borrowed successfully.")
                return
        else:
            print(f"Book '{book.book_name}' by {book.book_author} is not available in the library.")

    def return_book(self,book_nam,author_name,library):
                self.book_borrowed_list.remove(book_nam)
                library.book_list.append(Book(book_nam,author_name))
                print("Book successfully returned")