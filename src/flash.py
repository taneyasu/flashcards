import sqlite3

dbname = 'data/flashcards.db'
conn = sqlite3.connect(dbname)
conn.row_factory = sqlite3.Row
cur = conn.cursor()
flag = ''
while flag != 'f':
  cur.execute("SELECT * FROM flashcards where flag = 0 ORDER BY RANDOM() LIMIT 1")
  row = cur.fetchone()
  print(row['jap'])
  input('英訳を表示します。Enterを押してください。')
  print(row['eng'])
  ans = input('覚えていた場合は"y"を代入してください\n')
  if ans == 'y':
    cur.execute("UPDATE flashcards SET flag = 1 where id = ?", (row['id'],))
    conn.commit()
    ans = 'n'
  flag = input('次を表示します。終了する場合は"f"を代入してください\n')
cur.close()
conn.close()