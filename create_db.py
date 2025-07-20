import sqlite3
import pandas as pd
import pathlib

db_file = pathlib.Path("project.sqlite3")

def create_database():
    try:
        conn = sqlite3.connect(db_file)
        conn.close()
        print("✅ Database created successfully.")
    except sqlite3.Error as e:
        print("❌ Error creating database:", e)

def create_tables():
    try:
        with sqlite3.connect(db_file) as conn:
            sql_file = pathlib.Path("sql", "create_tables.sql")
            with open(sql_file, "r") as file:
                sql_script = file.read()
            conn.executescript(sql_script)
            print("✅ Tables created successfully.")
    except sqlite3.Error as e:
        print("❌ Error creating tables:", e)

def insert_data_from_csv():
    try:
        authors_df = pd.read_csv("data/authors.csv")
        books_df = pd.read_csv("data/books.csv")
        with sqlite3.connect(db_file) as conn:
            authors_df.to_sql("authors", conn, if_exists="replace", index=False)
            books_df.to_sql("books", conn, if_exists="replace", index=False)
            print("✅ Data inserted from CSV.")
    except Exception as e:
        print("❌ Error inserting data:", e)

def main():
    create_database()
    create_tables()
    insert_data_from_csv()

if __name__ == "__main__":
    main()
