import sqlite3

DB_FILE = "project.sqlite3"

def run_select_all():
    print("\n🔍 SELECT ALL BOOKS")
    with sqlite3.connect(DB_FILE) as conn:
        results = conn.execute("SELECT * FROM books;").fetchall()
        for row in results:
            print(row)

def run_join_query():
    print("\n🔗 JOIN AUTHORS AND BOOKS")
    with sqlite3.connect(DB_FILE) as conn:
        query = """
        SELECT authors.first, authors.last, books.title, books.year_published
        FROM authors
        INNER JOIN books ON authors.author_id = books.author_id;
        """
        results = conn.execute(query).fetchall()
        for row in results:
            print(row)

def run_update_query():
    print("\n✏️ UPDATE BOOK TITLE")
    with sqlite3.connect(DB_FILE) as conn:
        conn.execute("""
        UPDATE books
        SET title = 'To Kill a Mockingbird (Updated)'
        WHERE title = 'To Kill a Mockingbird';
        """)
        conn.commit()
        print("Updated title where needed.")

def run_delete_query():
    print("\n🗑️ DELETE OLD BOOKS (before 1950)")
    with sqlite3.connect(DB_FILE) as conn:
        conn.execute("DELETE FROM books WHERE year_published < 1950;")
        conn.commit()
        print("Deleted books published before 1950.")

def run_group_by_query():
    print("\n📊 BOOK COUNT BY AUTHOR")
    with sqlite3.connect(DB_FILE) as conn:
        query = """
        SELECT author_id, COUNT(*) AS book_count
        FROM books
        GROUP BY author_id;
        """
        results = conn.execute(query).fetchall()
        for row in results:
            print(row)
def main():
    run_select_all()
    run_join_query()
    run_update_query()
    run_delete_query()
    run_group_by_query()

if __name__ == "__main__":
    main()
