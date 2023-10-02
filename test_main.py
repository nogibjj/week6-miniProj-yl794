import sqlite3

if __name__ == "__main__":
    conn = sqlite3.connect('mydatabase.db')
    cursor = conn.cursor()
    cursor.execute("SELECT count(*) FROM users")
    num = cursor.fetchall()
    assert(num[0][0]==2)