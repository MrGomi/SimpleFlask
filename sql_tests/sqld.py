# executemany() method

# import the sqlite3 library
import sqlite3

# create a new database it the database doesn't aleady exist
with sqlite3.connect("new.db") as conn:
    # get the cursor object used to execute SQL commands
    c = conn.cursor()
     
    c.execute("SELECT city, state, population from population")

    # retrieve all records from the query
    rows = c.fetchall()

    # output the rows to the screen, row by row
    for r in rows:
        print r[0],r[1],r[2]
