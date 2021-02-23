import sqlite3
import check_table

dbname = 'data/flashcards.db'
conn = sqlite3.connect(dbname)
cur = conn.cursor()
check_table.show_table(dbname)

try:
  id_value = int(input('消去するidを入れてください\n'))
except:
  print("数字を入れてください。")
  sys.exit()

cur.execute('DELETE FROM flashcards where id = ?', (id_value,))

conn.commit()

cur.close()
conn.close()