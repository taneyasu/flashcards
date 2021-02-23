import sqlite3

def show_table(dbname):
  conn = sqlite3.connect(dbname)
  cur = conn.cursor()

  cur.execute('SELECT * FROM flashcards')

  print(cur.fetchall())

  cur.close()
  conn.close()

if __name__ == "__main__":
  show_table('data/flashcards.db')
