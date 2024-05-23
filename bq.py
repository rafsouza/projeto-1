
## tabela cliente 
import sqlite3
# Connect to the SQLite database
conn = sqlite3.connect('projeto_1.db')
cur = conn.cursor()
# Read the SQL script from the "projeto_1.sql" file
with open('projeto_1.sql', 'r', encoding='utf-8') as file:
    sql_script = file.read()
# Execute the SQL script to create and populate the tables
cur.executescript(sql_script)
# Query the "cliente" table to retrieve and print the data
cur.execute("SELECT * FROM cliente")
rows = cur.fetchall()
for row in rows:
    print(row)
# Close the connection to the database
conn.close()

conn = sqlite3.connect('projeto_1.db')
cur = conn.cursor()
# Query the "produto" table to retrieve and print the data
cur.execute("SELECT * FROM compra")
rows = cur.fetchall()
for row in rows:
    print(row)
# Close the connection to the database
conn.close()

