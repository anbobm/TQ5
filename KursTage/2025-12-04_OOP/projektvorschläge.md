## Personal Library Manager

A simple app to track books you own, what you’ve read, and reviews.
Database tables

books
* id (PK)
* title
* author_id (FK)
* genre_id (FK)
* year
* status ("unread", "reading", "read")

authors
* id (PK)
* name

genres
* id (PK)
* name

reviews
* id (PK)
* book_id (FK)
* rating (1–5)
* comment

Features
* Add/edit/delete books
* Mark reading status
* Search by title/author/genre
* Add reviews for finished books
* Simple CLI or Tkinter GUI


## Simple Expense Tracker

Track expenses by category, month, and payment method.
Database tables

expenses
* id (PK)
* amount
* date
* category_id (FK)
* payment_method_id (FK)
* notes

categories
* id (PK)
* name

payment_methods
* id (PK)
* name

Features
* Add new expenses
* View expenses by month
* Summaries: how much spent on each category
* Export to CSV
* Optionally: Matplotlib charts


## Student Course Registration System

Simulate how a small school registers students for courses.
Database tables

students
* id (PK)
* name
* email

courses
* id (PK)
* name
* instructor
* credits

enrollments
* student_id (FK)
* course_id (FK)
* PRIMARY KEY(student_id, course_id)

Features
* Add students & courses
* Students register for courses
* Prevent duplicate enrollments
* List all courses a student takes
* List all students in a course


## Inventory Management System (for a small shop)

Track products, suppliers, and stock levels.
Database tables

products
* id (PK)
* name
* price
* quantity
* supplier_id (FK)

suppliers
* id (PK)
* name
* email
* phone

orders
* id (PK)
* product_id (FK)
* quantity
* order_date

Features
* Add products/suppliers
* Update stock when orders arrive
* Low-stock alerts
* Search product catalog


## Movie Watchlist + Ratings App

Let users track movies they want to watch and rate completed ones.
Database tables

movies
* id (PK)
* title
* year
* genre_id (FK)

genres
* id (PK)
* name

watchlist
* id (PK)
* movie_id (FK)
* status ("want to watch", "watching", "finished")
* rating (nullable)

Features
* Search movies by title
* Change status
* Rate finished movies
* Top-rated movies list

