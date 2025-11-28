Library Management System

Project Title
Library Management System
A lightweight, console-based python application for managing library operations, perfect for beginners practicing core programming concepts.

Overview
This project implements a fully functional Library Management System using pure python, storing all data in memory with lists and dictionaries for simplicity. Users interact via a text-based menu to handle book inventory, member registration, borrowing, and returns, with real-time availability checks to prevent over-borrowing. Ideal for students, it reinforces python fundamentals like data structures, functions, loops, conditionals, and input validation while simulating real-world library workflows.The system allows tracking books by ID, title, and author, and manages which books are borrowed and by whom. It provides an interactive menu interface for the user to interact with the library's collection and members.

Features
-Book Operations: Add books (ID, title, author), display complete catalog with availability, track borrowed status.
-Member Operations: Register members (ID, name). list all members.
-Circulation Control: Borrow available books (links member to book), return books (frees for next user) view per-member borrowings.
- Validation: Blocks borrowing unavailable books; ensures unique IDs.

Planned Enhancements:
- File persistence (JSON/CSV/SQLite) for data retention.
- Advanced search (by title/author/genre).
- Deletion of books/members.
- Tkinter GUI for intuitive interface.
- Due dates, fines, and reports.

Technologies/Tools Used
-Language: Python (no external libraries needed).
-Storage: Lists for collections; dictionaries for relational data (e.g., book-to-member mapping).
-UI: Terminal menu with `input()`/`print()` for choices 1-8.
-Concepts Demonstrated: Modular functions, while loops for menus, try-except for error handling, list comprehensions.

Installation & Setup
1. Verify python installation: `python --version`.
2. Save code as `library_system.py`.
3. Navigate to directory: `cd path/to/project`.
4. Launch: `python library_system.py`.
5. Select menu options (1=add book, etc.); follow prompts for inputs.

Testing Instructions
- Basic Flow: Add book (ID:101, "Python Basics", "AuthorX"), add member (ID:1, "UserA"), borrow (confirms "Issued to UserA"), return (resets to available).
- View Functions: List books/members, check borrowing report.
- Error Handling: Borrow non-existent/unavailable book (displays error), invalid inputs prompt retry.
- Full Cycle: Repeat 5-10 operations; restart to observe data reset.
- Metrics: Test 20+ books/members for performance (handles efficiently in memory).


