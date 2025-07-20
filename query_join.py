import sqlite3

def run_join_query():
    with sqlite3.connect("project.sqlite3") as conn:
        cursor = conn.cursor()
        query = """
        SELECT authors.first, authors.last, books.title
        FROM authors
        INNER JOIN books ON authors.author_id = books.author_id;
        """
        results = cursor.execute(query).fetchall()
        for row in results:
            print(row)

if __name__ == "__main__":
    run_join_query()

