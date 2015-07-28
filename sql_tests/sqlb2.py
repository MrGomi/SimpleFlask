# Create a SQLite3 database and table

# import the sqlite3 library
import sqlite3

# create a new database it the database doesn't aleady exist
with sqlite3.connect("new.db") as conn:
    # get the cursor object used to execute SQL commands
    c = conn.cursor()

    # create a table 
    c.execute("INSERT INTO population VALUES('Berlin', 'BER', 3400000)")
    c.execute("INSERT INTO population VALUES('Hamburg', 'HA', 100000)")
