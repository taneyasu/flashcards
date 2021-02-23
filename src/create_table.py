import sqlite3

dbname = 'data/flashcards.db'
conn = sqlite3.connect(dbname)
cur = conn.cursor()

cur.execute(
  'CREATE TABLE flashcards(id INTEGER PRIMARY KEY, jap TEXT, eng TEXT, flag int default 0)'
)

conn.commit()
conn.close()