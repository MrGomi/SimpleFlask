# executemany() method

# import the sqlite3 library
import sqlite3

# create a new database it the database doesn't aleady exist
with sqlite3.connect("new.db") as conn:
    # get the cursor object used to execute SQL commands
    c = conn.cursor()
    # insert multiple records using a tuple
    cities = [
            ('Boston', 'MA', 600000),
            ('Chicago', 'IL', 270000),
            ('Houston', 'TX', 2100000),
            ('Phoenix', 'AZ', 150000)
            ]
    # insert data into table
    c.executemany("INSERT INTO population VALUES(?,?,?)", cities)