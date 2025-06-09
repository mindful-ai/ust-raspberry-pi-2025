📝 Problem Statement:

You are asked to implement a simple Library Management System. The system should allow users to borrow and return books.

Design a class Library with the following requirements:

✅ Functional Requirements

A Library is initialized with a collection of book titles (strings).

A user can:
Borrow a book (only if available).
Return a book.
When a book is borrowed, it should no longer be available.
If a book is returned, it should be added back to the available collection.
If a user tries to borrow a book that is not available, raise a BookNotAvailableError.
If a user tries to return a book that wasn’t borrowed, raise a InvalidReturnError.

✅ Implementation Requirements

Define a class Library
Define two custom exceptions:
BookNotAvailableError
InvalidReturnError

✅ Write Test Cases (Using pytest)

Write a test suite (test_library.py) that:

    Tests successful borrow and return
    Tests for unavailable book borrowing
    Tests for invalid book return