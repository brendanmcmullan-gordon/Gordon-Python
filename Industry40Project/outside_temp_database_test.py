import sqlite3

database = sqlite3.connect('example.db')

cursor = database.cursor()

# cursor.execute('''CREATE TABLE stocks
# (date text, trans text, symbol text, qty real, price real)''')
#
# cursor.execute("INSERT INTO stocks VALUES ('2019-04-29', 'BUY', 'GRD', 100, 44)")
#
# database.commit()
#
# database.close()

# cursor.execute('SELECT * FROM stocks')
#
# print(cursor.fetchone())


# cursor.execute("INSERT INTO stocks VALUES ('2019-04-29', 'BUY', 'ABC', 50, 30)")
# cursor.execute("INSERT INTO stocks VALUES ('2019-04-29', 'BUY', 'XYZ', 10, 100)")

cursor.execute('SELECT * FROM stocks')

for r in cursor.execute('SELECT * FROM stocks'):
    print(r)

database.commit()

database.close()
