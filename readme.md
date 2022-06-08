Project prerequisites:
1. open command prompt and type "python -m venv venv" to create a virtual environment.
2. Type "venv\Scripts\activate" to activate virtual env. Note: 'S' in 'Scripts' must be capital.
3. After activating virtual env , type "pip install django" to install django.
4. navigate to the parent folder contains the file 'manage.py' and type "python manage.py runserver" . Server will be started...
5. open the link displayed as result.

UI Explanation and manupulation: 
We have five buttons namely "Add Author","Add Books","Book and Author","Author and Book","Author and Books Count".
 The first two mandatory steps to move forward is to Add authors and Add books which is done by the two options 
 available:
- When we consider the first option that is Add Author,it is used to add authors in the terminal.
- When we click on the second option that is Add Books, it is used to add books in the terminal.

- After adding authors and books when we click on the third option that is "Book and Author" it will print all the 
author's name and the book written by him from the database to the console.

- When we click on the fourth option that is "Author and Book" it will print author's name and all the books he/she 
wrote to the console.

- When we click on the last option that is "Author and Books count" it will print the count of books written by the
author to the console.
