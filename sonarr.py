import sqlite3

def main():
    # Hardcoded database file (Security Issue)
    db_file = "users.db"

    conn = sqlite3.connect(db_file)
    cursor = conn.cursor()

    # Table creation without constraints (Maintainability Issue)
    cursor.execute("CREATE TABLE IF NOT EXISTS users (id INTEGER, username TEXT, password TEXT)")

    # Taking raw input from user
    username = input("Enter username: ")

    # SQL Injection vulnerability (Security Issue)
    query = f"SELECT * FROM users WHERE username = '{username}'"
    cursor.execute(query)

    rows = cursor.fetchall()
    for row in rows:
        print("User:", row[1])

    # Resource leak: connection not closed (Maintainability Issue)

if __name__ == "__main__":
    try:
        main()
    except Exception as e:  # Catching generic Exception (Maintainability Issue)
        print("Error occurred:", e)

