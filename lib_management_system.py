class Library:
    def __init__(self):
        self.books = []
        self.members = [] 
        self.borrowed = []


    def add_book(self):
        book_id = input("Enter Book ID: ")
        title = input("Enter Book Title: ")
        author = input("Enter Author Name: ")

        self.books.append({
            "id": book_id,
            "title": title,
            "author": author,
            "available": True
        })

        print("\n Book added successfully!\n")

    def view_books(self):
        if not self.books:
            print("No books available.\n")
            return

        print("\n------ AVAILABLE BOOKS ------")
        for b in self.books:
            if b["available"]:
                status = "Available"
            else:
                status = "Borrowed"
            print(f"ID: {b['id']} | {b['title']} by {b['author']} | {status}")
        print()


    def add_member(self):
        member_id = input("Enter Member ID: ")
        name = input("Enter Member Name: ")

        self.members.append({
            "id": member_id,
            "name": name
        })

        print("\n Member added successfully!\n")

    def view_members(self):
        if not self.members:
            print("No members registered.\n")
            return

        print("\n------ MEMBERS LIST ------")
        for m in self.members:
            print(f"ID: {m['id']} | Name: {m['name']}")
        print()


    def borrow_book(self):
        book_id = input("Enter book ID to borrow: ")
        member_id = input("Enter member ID: ")

        book = None
        for b in self.books:
            if b["id"] == book_id:
                book = b
                break
        
        member = None
        for m in self.members:
            if m["id"] == member_id:
                member = m
                break

        if not book:
            print("Book not found.\n")
            return
        if not member:
            print("Member not found.\n")
            return
        if not book["available"]:
            print("Book already borrowed.\n")
            return

        book["available"] = False
        self.borrowed.append({"book_id": book_id, "member_id": member_id})

        print(f"\n '{book['title']}' issued to {member['name']}.\n")

    def return_book(self):
        book_id = input("Enter Book ID to return: ")

        book = None
        for b in self.books:
            if b["id"] == book_id:
                book = b
                break

        if not book:
            print("Book not found.\n")
            return

        if book["available"]:
            print("Book was not borrowed.\n")
            return

        book["available"] = True

        self.borrowed = [b for b in self.borrowed if b["book_id"] != book_id]

        print("Book returned successfully! \n")

    def view_borrowed(self):
        if not self.borrowed:
            print("No borrowed books.\n")
            return

        print("\n------ BORROWED BOOKS ------")
        for rec in self.borrowed:
            book = None
            for b in self.books:
                if b["id"] == rec["book_id"]:
                    book = b
                    break
            member = None
            for m in self.members:
                if m["id"] == rec["member_id"]:
                    member = m
                    break
            print(f"Book: {book['title']} | Borrowed by: {member['name']}")
        print()


    def run(self):
        while True:
            print("""
==================================
      LIBRARY MANAGEMENT SYSTEM
----------------------------------
1. Add Book
2. View Books
3. Add Member
4. View Members
5. Borrow Book
6. Return Book
7. View Borrowed Books
8. Exit
==================================
""")
            choice = input("Enter choice: ")

            if choice == '1':
                self.add_book()
            elif choice == '2':
                self.view_books()
            elif choice == '3':
                self.add_member()
            elif choice == '4':
                self.view_members()
            elif choice == '5':
                self.borrow_book()
            elif choice == '6':
                self.return_book()
            elif choice == '7':
                self.view_borrowed()
            elif choice == '8':
                print("\nExiting system… \n")
                break
            else:
                print("Invalid choice! Try again.\n")


# Run Application
lib = Library()
lib.run()