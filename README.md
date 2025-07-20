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
<img width="1572" height="877" alt="image" src="https://github.com/user-attachments/assets/b7493864-75d0-48d0-8f24-46ed8e14be4b" />

<img width="1625" height="888" alt="image" src="https://github.com/user-attachments/assets/12c476fa-1f40-4b3f-89d9-3ee71a5d9feb" />


