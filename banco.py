import sqlite3
# Connect to the SQLite database
conn = sqlite3.connect('projeto_1.db')
cur = conn.cursor()
# Get the table names from the database
cur.execute("SELECT name FROM sqlite_master WHERE type='table';")
tables = cur.fetchall()
# Iterate over each table and read its data
for table in tables:
    table_name = table[0]
    print(f"Reading data from table: {table_name}")
    cur.execute(f"SELECT * FROM {table_name}")
    rows = cur.fetchall()
    for row in rows:
        print(row)
# Close the connection to the database
conn.close()