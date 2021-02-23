import sqlite3
import sys


flag = ''

dbname = 'data/flashcards.db'
conn = sqlite3.connect(dbname)
cur = conn.cursor()

while flag != 'f':
  try:
    id_value = int(input('idを入れてください。\n'))
    jap_text = input('日本文を入れてください。\n')
    eng_text = input('英訳を入れてください。\n')
  except:
    print("エラー：数字を入れてください。")
  try:
    cur.execute('INSERT INTO flashcards(id,jap,eng) values(?,?,?)',(id_value,jap_text,eng_text))
  except:
    print('エラー:同じidを使用している可能性があります。')
  conn.commit()
  flag = input("終了する場合は'f'を代入してください。")

cur.close()
conn.close()