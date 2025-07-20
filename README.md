# datafun-05-sql

## Author
Robert Davis

## Description
Python + SQL project using SQLite and pandas.

## Setup
- Clone the repo
- Create a virtual environment: `python -m venv .venv`
- Activate it: `.venv\Scripts\Activate.ps1`
- Install dependencies: `pip install -r requirements.txt`
# 📊 DataFun-05: SQL & Python Project

## 👤 Your Info
- **Name:** Robert Davis
- **Course:** Business Intelligence
- **Project Repo:** [datafun-05-sql](https://github.com/Robert-Davis18118/datafun-05-sql)

---

## 📁 Folder Structure

datafun-05-sql/
│
├── data/
│ ├── authors.csv
│ └── books.csv
│
├── scripts/
│ └── create_tables.sql
│
├── project.sqlite3
├── create_db.py
├── query_all.py
├── README.md
└── requirements.txt

---

## 🧪 Core SQL Skills Demonstrated

### 1. ✅ SELECT All Records
```sql
SELECT * FROM books;
SELECT authors.first, authors.last, books.title
FROM authors
INNER JOIN books ON authors.author_id = books.author_id;
UPDATE books
SET title = 'To Kill a Mockingbird (Updated)'
WHERE title = 'To Kill a Mockingbird';
DELETE FROM books
WHERE year_published < 1950;
SELECT author_id, COUNT(*) AS book_count
FROM books
GROUP BY author_id;



