# Create a SQLite3 database and table

# import the sqlite3 library
import sqlite3

# create a new database it the database doesn't aleady exist
conn = sqlite3.connect("new.db")

# get the cursor object used to execute SQL commands
c = conn.cursor()

# create a table 
c.execute("""CREATE TABLE population
            (city TEXT, state TEXT, population INT)
        """)

# close the database connection
conn.close()