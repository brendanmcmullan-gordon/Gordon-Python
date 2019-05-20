import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="Password1"
)

print(db)

# Create an SQL 'cursor'
c = db.cursor()


# Create a DB
# c.execute("CREATE DATABASE sensors")

# List DBs
# c.execute("SHOW DATABASES")
# for x in c
#   print(x)

# Create a Table
# c.execute("CREATE TABLE weather (temperature VARCHAR(255), other VARCHAR(255))")

# List Tables
# c.execute("SHOW TABLES")
# for x in c
#     print(x)

# Add a column (add a unique id column)
# c.execute("ALTER TABLE weather ADD COLUMN id INT AUTO_INCREMENT PRIMARY KEY")

# Insert table entries
sql = "INSERT INTO weather (OUTSIDETEMP) VALUES (%s)"
val = ("30.6",)
c.execute(sql, val)
db.commit()


