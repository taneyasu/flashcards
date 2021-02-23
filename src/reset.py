import sqlite3

dbname = 'data/flashcards.db'
conn = sqlite3.connect(dbname)
cur = conn.cursor()

cur.execute("UPDATE flashcards set flag = 0")
conn.commit()

cur.close()
conn.close()
