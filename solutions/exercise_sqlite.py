import sqlite3

conn = sqlite3.connect('example.db')
c = conn.cursor()

c.execute("""DROP TABLE stocks""")

c.execute("""CREATE TABLE stocks
          (date text, trans text, symbol text, qty real, price real)""")

c.execute("""INSERT INTO stocks 
          VALUES ('2006-01-05', 'BUY', 'RHAT', 100, 35.14)""")
c.execute("""INSERT INTO stocks 
          VALUES ('2006-01-06', 'BUY', 'RHAT', 100, 34.14)""")
c.execute("""INSERT INTO stocks 
          VALUES ('2006-01-07', 'BUY', 'RHAT', 100, 33.14)""")

conn.commit()

for row in c.execute('SELECT * FROM stocks WHERE price > 35 ORDER BY price'):
     print(row)

conn.close()
