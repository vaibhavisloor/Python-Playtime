# Create 3 members. Make 1 member to borrow 2 books. and return 1. 
from library import Book,Library
from member import Member

Lib1 = Library()

Lib1.add_book('Hyperfocus','Chris Bailey')
Lib1.show_books() #Shows books in library

    
member1=Member("Vaibhav",9900855730)

member1.borrow_book('Hyperfocus', Lib1)

Lib1.show_books() #Shows books in library

member1.return_book('Hyperfocus','Chris Bailey',Lib1)

Lib1.show_books() #Shows books in library