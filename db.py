import sqlite3

# create a new database and open a 
# database connection to allow sqlite3 
# to work with it
con = sqlite3.connect("users.db")

# In order to execute SQL statements 
# and fetch results from SQL queries, 
# we will need to use a database cursor.
cur = con.cursor()

# create a table in the dataase
#cur.execute("CREATE TABLE users(first_name, last_name, age, email)")

res = cur.execute("SELECT name FROM sqlite_master")
print(res.fetchone())