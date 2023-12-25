class Book:
    def __init__(self,book_name,book_author):
        self.book_name = book_name
        self.book_author = book_author

class Library:
    def __init__(self):
        self.number_of_books = 10
        self.book_list = [
        Book("The Great Gatsby", "F. Scott Fitzgerald"),
        Book("To Kill a Mockingbird", "Harper Lee"),
        Book("1984", "George Orwell"),
        Book("Pride and Prejudice", "Jane Austen"),
        Book("The Catcher in the Rye", "J.D. Salinger"),
        Book("Harry Potter and the Sorcerer's Stone", "J.K. Rowling"),
        Book("The Lord of the Rings", "J.R.R. Tolkien"),
        Book("The Hobbit", "J.R.R. Tolkien"),
        Book("The Chronicles of Narnia", "C.S. Lewis"),
        Book("The Da Vinci Code", "Dan Brown")
        ]

    def show_books(self):
        for book in self.book_list :
            print(f"Book Name : {book.book_name}") 
        print("/n")       


    def add_book(self,bookname,authorname):
        self.book_list.append(Book(bookname,authorname))

    def remove_book(self,bookname,authorname):
        for book in self.book_list:
            if book.book_name == bookname and book.book_author == authorname:
                self.book_list.remove(book)
                return
        print("Book not found")
        

       