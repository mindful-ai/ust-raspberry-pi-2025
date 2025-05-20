Session #1 [20+20]
-----------------------------------------------------------------------------------------

1. Tkinter Application for Determining if the input is a prime number
2. Tkinter Application for Temperature Conversion

Session #2 [60]: To-Do App (Tkinter + SQLite3)
-----------------------------------------------------------------------------------------

🔹 Problem Statement:

Design a To-Do List application using Tkinter and sqlite3. The app should:

    Allow the user to add tasks.
    Show a list of saved tasks in a Listbox.
    Allow deleting selected tasks.
    Save tasks persistently in an SQLite database.

✅ Solution Summary:

    Use sqlite3 to create a table tasks.
    Fetch tasks on startup and display in Listbox.
    Add task: INSERT into DB and update Listbox.
    Delete task: DELETE from DB using task name or ID.