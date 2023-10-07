import sqlite3
    
if __name__ == "__main__":
    conn = sqlite3.connect("Chinook.sqlite")
    cursor = conn.cursor()
    with open("query.sql", 'r', encoding="utf-8") as f:
        sql_content = f.read()
    cursor.execute(sql_content)
    results = cursor.fetchall()
    conn.commit()
    for row in results:
        print(row)
    
    # Close the connection
    conn.close()
